import datetime
import logging

from hashlib import sha256

logger = logging.getLogger(__name__)


class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = (
            str(self.time_stamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        block_hash = sha256(block_header.encode()).hexdigest()
        return block_hash

    def print_contents(self):
        logger.info(f"Transactions: {self.transactions}")
        logger.info(f"Current Hash: {self.hash}")
        logger.info(f"Previous Hash: {self.previous_hash}")
        logger.info(f"Timestamp: {self.time_stamp}")
