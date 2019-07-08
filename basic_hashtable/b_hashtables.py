

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity # Max size
        self.count = 0  # Current size being used
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
	# a good number to start with, especially if `string` is short
    hash = 5381

    for i in string:
    	# `(hash << 5) + hash` == `hash * 33`
    	hash = ((hash << 5) + hash) ^ ord(i)

    # print('hash:', hash, len(str(hash)))
    # print('hash &:', hash & 0xFFFFFFFF, len(str(hash & 0xFFFFFFFF)))
    # print('hash % max', hash % max, len(str(hash % max)))

    return hash % max


	# const MAGIC_CONSTANT = 5381;

	# const djb2a = string => {
	# 	let hash = MAGIC_CONSTANT;

	# 	for (let i = 0; i < string.length; i++) {
	# 		// Equivalent to: `hash * 33 ^ string.charCodeAt(i)`
	# 		hash = ((hash << 5) + hash) ^ string.charCodeAt(i);
	# 	}

	# 	// Convert it to an unsigned 32-bit integer
	# 	return hash >>> 0;
	# };


	# def hash_djb2(s):                                                                                                                                
	#     hash = 5381
	#     for x in s:
	#         hash = (( hash << 5) + hash) + ord(x)
	# 	return hash & 0xFFFFFFFF

	# def djb2(base, word):
	#     ''' Hash a word using the djb2 algorithm with the specified base. '''
	#     for c in word:
	#         base = ((base << 5) + base + ord(c)) & 0xffffffff
	# 	return base


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash the key
    # check HT index for hashed index
    # if not None and HT[hashed index][0] != key
    # assign value to HT index

    hashed_index = hash(key, hash_table.capacity)

    if hash_table.storage[hashed_index] and hash_table.storage[hashed_index][0] != key:
    	print(f'Overwriting key {hash_table.storage[hashed_index][0]} with {key}!')

    hash_table.storage[hashed_index] = (key, value)

    return


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    if not hash_table.storage[hashed_index]:
    	return print(f'Key {key} not found!')

    hash_table.storage[hashed_index] = None

    return


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    retrieved = hash_table.storage[hashed_index]

    if retrieved:
    	return retrieved[1]
    else:
    	return retrieved


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    print(hash_table_retrieve(ht, "line"))

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
