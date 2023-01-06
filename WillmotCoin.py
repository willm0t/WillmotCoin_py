# https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode() +
                   str(self.timestamp).encode() +
                   str(self.data).encode() +
                   str(self.previous_hash).encode())
        return sha.hexdigest()


def create_genesis_block():
    # creates the first block in the chain ("Genesis Block")
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(prev_block):
    this_index = prev_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is Block " + str(this_index)
    this_hash = prev_block.hash
    return Block (this_index, this_timestamp, this_data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks = 5

for i in range(0, num_of_blocks):
    blocks_to_add = next_block(previous_block)
    blockchain.append(blocks_to_add)
    previous_block = blocks_to_add
    print("Block #{} has been added".format(blocks_to_add.index))
    print("Hash: {}\n".format(blocks_to_add.hash))