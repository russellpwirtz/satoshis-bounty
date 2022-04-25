import hashlib 
import binascii 

def get_word_list():
    with open("wordlist/english.txt", "r") as f:
        return [w.strip() for w in f.readlines()]

def generate_random_entropy():
    return "a10ec20dc3af2f652c7fac2f1230f1a3" # 32 hex chars; 12 words

def generate_seedphrase():
    words = get_word_list()
    entropy = generate_random_entropy()
    data = entropy.strip()
    data = binascii.unhexlify(data)
    if len(data) not in [16, 20, 24, 28, 32]:
        raise ValueError("Data length should be one of the following: [16, 20, 24, 28, 32], but it is not: " + str(len(data)))
    h = hashlib.sha256(data).hexdigest()
    b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]
    seed = []
    for i in range(len(b)//11):
        indx = int(b[11*i:11*(i+1)],2)
        seed.append(words[indx])
    return seed