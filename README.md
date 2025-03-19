This project is a simple implementation of a blockchain system in Python. It allows you to create multiple blockchains, add data to them, and validate the integrity of the chains. 
Out of curiosity of how to optimize data storage and mining, I wanted to see if blockchain would be a great alternative to data storage.

Table of Contents
----------------
1. Project Structure
2. Features
3. Installation
4. Usage
5. Extending the Project
6. License

Project Structure
-------------------
blockchain_project/
│
├── blockchain.py          # Contains Block, Blockchain, and BlockchainManager classes
├── main.py                # Example usage and execution of the blockchain
└── README.md              # Documentation

Features
----------
- Block Class:
      - Represents a single block in the blockchain. Each block contains:
      - Index
      - Previous block hash
      - Data
      - Timestamp
      - Current block hash

- Blockchain Class:
    - Manages a chain of blocks. Provides functionality to:
    - Creates a genesis block
    - Adds new blocks
    - Validate the integrity of the blockchain

- BlockchainManager Class:
    - Manages multiple blockchains. Allows you to:
    - Create new blockchains
    - Add data to specific blockchains
    - Retrieve blockchains by index

Installation
------------------
Clone the repository:

git clone https://github.com/your-username/blockchain-project.git
cd blockchain-project
Ensure you have Python installed (version 3.6 or higher).

Run the project:

- python main.py
- Usage
- Creating Blockchains
- You can create multiple blockchains using the BlockchainManager class. Each blockchain is independent and can store its own data.

Adding Data
Use the add_block_to_blockchain method to add data to a specific blockchain.

Validating Blockchains
The is_chain_valid method checks the integrity of a blockchain by verifying the hashes of all blocks.

Example
Here’s an example of how to use the project:

python
Copy
from blockchain import BlockchainManager

def main():
    manager = BlockchainManager()

    # Create the first blockchain
    blockchain1 = manager.create_new_blockchain()
    manager.add_block_to_blockchain(0, "Data for Blockchain 1, Block 1")
    manager.add_block_to_blockchain(0, "Data for Blockchain 1, Block 2")

    # Create a second blockchain
    blockchain2 = manager.create_new_blockchain()
    manager.add_block_to_blockchain(1, "Data for Blockchain 2, Block 1")
    manager.add_block_to_blockchain(1, "Data for Blockchain 2, Block 2")

    # Print the contents of the first blockchain
    print("Blockchain 1:")
    for block in blockchain1.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")

    # Print the contents of the second blockchain
    print("\nBlockchain 2:")
    for block in blockchain2.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")

    # Check if the blockchains are valid
    print("\nIs Blockchain 1 valid?", blockchain1.is_chain_valid())
    print("Is Blockchain 2 valid?", blockchain2.is_chain_valid())

if __name__ == "__main__":
    main()
    
Extending the Project
------------------------
You can extend this project by adding features such as:

Persistence: Save blockchains to a file or database.

Consensus Algorithms: Implement Proof of Work or Proof of Stake.

Networking: Create a peer-to-peer network for decentralized blockchains.

Command-Line Interface (CLI): Build a CLI for interacting with the blockchains.

License
-----------
This project is licensed under the MIT License. See the LICENSE file for details.

