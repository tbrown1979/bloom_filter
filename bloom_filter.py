from hashlib import sha1

class HashGenerator():
    self.uniqueKey = 0
    self.salt = "salty"

    def generateHash(m):
        def hashFunction = 
            hashed = sha1(str(self.uniqueKey) + self.salt)
            num = int(hashed[0:9], 16) % m
            return num
        return hashFunction
    