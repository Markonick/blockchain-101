import logging

from block import Block

logger = logging.getLogger(__name__)


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(transactions=[], previous_hash="0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        self.chain.append(new_block)

    def print_blocks(self):
        for i in range(len(self.chain)):
            logger.info(f"Block {i}: {self.chain[i].hash}")
            current_block = self.chain[i]
            current_block.print_contents()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.generate_hash():
                logger.warning(
                    "Current hash does not match generated hash, because of tampering with the block"
                )
                return False
            if current_block.previous_hash != previous_block.hash:
                logger.warning("Previous hash does not match, hash got manipulated")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while not proof.startswith("0" * difficulty):
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
