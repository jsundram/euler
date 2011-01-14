#!/usr/bin/env python
# encoding: utf-8
"""
059 - Decryption.py

Created by Jason Sundram on 2009-12-18.
Copyright (c) 2009. All rights reserved.

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 

For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; 
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain
common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
from timed import timed

def decode(c, b):
    return c ^ b


def decode_bytes(bytes, password):
    n = len(password)
    p = map(ord, password)
    return [decode(p[i % n], b) for (i, b) in enumerate(bytes)]


def valid(c):
    """Is c a valid decrypted character?"""
    # look at http://www.asciitable.com/ for an ascii table
    # Tried 32-122, but too many decryptions were possible. 
    s = set(range(32, 123))
    s.remove(ord('`'))
    return c in s


def can_decrypt(bytes, c, n, N):
    """Test if c is the right character for position n (n is the 0-based index in the N char password)"""
    for (i, b) in enumerate(bytes):
        if i % N == n and not valid(decode(c, b)):
            return False
    return True

def read_bytes(filename):
    f = open(filename)
    ciphertext = f.readlines()[0]
    f.close()
    return map(int, ciphertext.strip().split(',')) # file has comma-separated ascii values, terminated by \r\n

@timed
def original_solution():
    bytes = read_bytes('059 - Decryption.txt')
    
    # Given: the password is lowercase a-z, and 3 letters long
    N, C = 3, range(ord('a'), ord('z')+1)
    
    password = ''.join([chr(c) for i in range(N) for c in C if can_decrypt(bytes, c, i, N)])
    
    assert(len(password) == N)
    
    decoded = decode_bytes(bytes, password)
    
    print "Password: %s\nText:\n%s" % (password, ''.join(map(chr, decoded)))
    
    return sum(decoded)


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

