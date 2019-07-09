

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.original_capacity = capacity
        # self.count = 0
        self.storage = [None] * capacity


# '''
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


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed_index = hash(key, hash_table.capacity)

    # check for Pair at hashed index
    # if not pair, make it, then return
    # if pair, iterate through `next` until None
    # make pair, then return

    item = hash_table.storage[hashed_index]

    if not item:
        hash_table.storage[hashed_index] = LinkedPair(key, value)
        return

    while True:
        print('item:', item, 'item.next', item.next)
        if item.key == key:
            item.value = value
            return
        elif item.next:
            item = item.next
            continue
        else:
            item.next = LinkedPair(key, value)
            return


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    item = hash_table.storage[hashed_index]

    if not item:
        return print(f'Key {key} not found!')

    if item.key == key:
        hash_table.storage[hashed_index] = item.next
        return

    while True:
        # print('removing:', key, 'current item:', item, 'item.next', item.next)
        
        if item.next.key == key:
            item.next = item.next.next
            return
        elif not item.next:
            return print(f'Key {key} not found!')
        else:
            item = item.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)

    item = hash_table.storage[hashed_index]

    

    while True:
        if not item:
            return print(f'Key {key} not found!')
        # print('retrieving:', key, 'current item:', item, 'item.next', item.next)
        
        if item.key == key:
            return item.value
        else:
            item = item.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # double the size of the hash_table

    # create new hash table
    # iterate over old HT
    # insert each value in new HT

    new_hash_table = HashTable(hash_table.capacity * 2)

    for i in hash_table.storage:
        item = i
        while item:
            hash_table_insert(new_hash_table, item.key, item.value)
            item = item.next

    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
