import hashlib 
import binascii
import random 

def get_word_list():
    with open("wordlist/english.txt", "r") as f:
        return [w.strip() for w in f.readlines()]

def generate_entropy():
    return binascii.unhexlify(str(hex(random.getrandbits(128))).removeprefix('0x').strip())

def generate_seedphrase(wordlist):
    try:
        data = generate_entropy()
    except Exception as e: 
        print('[Will retry] Failed to generate seedphrase: '+ str(e)) # TODO fix bug
        data = generate_entropy()

    if len(data) not in [16, 20, 24, 28, 32]:
        print("[Will retry] Data length should be one of the following: [16, 20, 24, 28, 32], but it is not: " + str(len(data))) # TODO fix bug
        data = generate_entropy()

    if len(data) not in [16, 20, 24, 28, 32]:
        raise ValueError("Data length should be one of the following: [16, 20, 24, 28, 32], but it is not: " + str(len(data)))

    h = hashlib.sha256(data).hexdigest()
    b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]
    seed = []
    for i in range(len(b)//11):
        indx = int(b[11*i:11*(i+1)],2)
        seed.append(wordlist[indx])
    return seed