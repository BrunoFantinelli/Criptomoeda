import hashlib
import time
import binascii

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

class Blockchain:
    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)
        self.DIFFICULTY_ADJUSTMENT = 10
        self.BLOCK_INTERVAL = 120

    def getLastestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generateNextBlock(self, data):
        previousBlock = self.getLastestBlock()
        nextIndex = previousBlock.index + 1
        nextTimestamp = int(round(time.time() * 1000))
        nextPreviousHash = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimestamp, data, calculateHash(nextIndex, nextPreviousHash, nextTimestamp, data))

        if self.validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validatingBlock(self, newBlock):
        previousBlock = self.getLastestBlock()
        if previousBlock.index + 1 != newBlock.index:
            return False
        elif previousBlock.hash != newBlock.previousHash:
            return False
        return True

    def hashMatchesDifficulty(self, hash, difficulty):
        hashBinary = binascii.unhexlify(hash)
        requeriedPrefix = '0'*int(difficulty)
        return hashBinary.startswith(requeriedPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(inde, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDifficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp, data, difficulty, nonce)
                return block
            nonce = nonce + 1

    def getDifficulty(self):
        latestBlock = self.getLastestBlock()
        if latestBlock.index % self.DIFFICULTY_ADJUSTMENT == 0 and latestBlock.index != 0:
            return self.getAdjustedDifficulty()
        else:
            return lastestBlock.difficulty

    def getAdjustedDifficulty(self):
        lastestBlock = self.getLastestBlock()
        previousAdjustmentBlock = self.blockchain[len(self.blockchain) - self.DIFFICULTY_ADJUSTMENT]
        timeExpected = self.BLOCK_INTERVAL * self.DIFFICULTY_ADJUSTMENT
        timeTaken = latestBlock.timestamp - previousAdjustmentBlock.timestamp
        if timeTaken < timeExpected * 2:
            return previousAdjustmentBlock.difficulty + 1
        elif timeTaken > timeExpected * 2:
            return previousAdjustmentBlock.difficulty - 1
        else:
            return previousAdjustmentBlock.difficulty

def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
    return hashlib.sha256((str(index) + previousHash + str(timestamp) + data + str(difficulty + str(nonce))).encode('utf-8')).hexdigest()

ts = int(round(time.time() * 1000))
genesisBlock = Block(0, "", ts, "Genesis block", calculateHash(0, "", ts, "Genesis block"))
