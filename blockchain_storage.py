import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash  
        self.data = data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (f"{self.index}"
                        f"{self.previous_hash}"
                        f"{self.data}"
                        f"{self.timestamp}")
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, data, 
                          time.time())
        self.chain.append(new_block)

    def chain_validity(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self[i - 1]

            if current_block.hash != current_block.calculate():
                print("Current block hash is invalid")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print("Previous block hash is invalid!")
                return False
            
        return True
    

class BlockchainManager:
    def __init__(self):
        self.blockchains = []

    def create_new_blockchain(self):
        new_blockchain = Blockchain()
        self.blockchains.append(new_blockchain)
        return new_blockchain
    
    def add_block_to_blockchain(self, blockchain_index, data):
        if blockchain_index < len(self.blockchains):
            self.blockchains[blockchain_index].add_block(data)
        else:
            print("Blockchain index is out of range!")

    def get_blockchain(self, blockchain_index):
        if blockchain_index < len(self.blockchains):
            return self.blockchains[blockchain_index]
        else:
            print("Blockchain index is out of range!")
            return None