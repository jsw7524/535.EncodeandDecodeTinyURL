import hashlib
class Codec:
    def __init__(self):
        self.dictionary = {};

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        longUrlmd5=hashlib.md5(longUrl).hexdigest()
        self.dictionary[longUrlmd5[:8]]=longUrl
        return longUrlmd5[:8]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.dictionary[shortUrl];

# Your Codec object will be instantiated and called as such:
url="https://leetcode.com/problems/design-tinyurl".encode("utf-8")
codec = Codec()
print(codec.decode(codec.encode(url)))


