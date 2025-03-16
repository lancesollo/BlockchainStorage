import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Simple PoW
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            prev_block = self.chain[i - 1]
            if block['previous_hash'] != hashlib.sha256(json.dumps(prev_block, sort_keys=True).encode()).hexdigest():
                return False
            proof_diff = block['proof']**2 - prev_block['proof']**2
            if not hashlib.sha256(str(proof_diff).encode()).hexdigest()[:4] == "0000":
                return False
        return True

# Creates and tests the blockchain
blockchain = Blockchain()
print("Genesis Block:", blockchain.chain)

# Adds blocks
proof = blockchain.proof_of_work(blockchain.get_previous_block()['proof'])
blockchain.create_block(proof, hashlib.sha256(json.dumps(blockchain.get_previous_block(), sort_keys=True).encode()).hexdigest())
print("Updated Blockchain:", blockchain.chain)

# Validates the chain
print("Is chain valid?", blockchain.is_chain_valid())
