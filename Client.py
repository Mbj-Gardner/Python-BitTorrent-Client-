import sys
import bencoder
import hashlib

file_in = sys.argv[1] # take torrent as input from command line
torrent = open(f'C:/Users/Mister Gardner/Desktop/BitTorrent client project/{file_in}', 'rb')
data = torrent.read()
file_data = bencoder.decode(data) #decode bencoded torrent file
new_dict = {}
key_set=()
wanted_keys = {b'piece length', b'pieces', b'name', b'length', b'files'} # required keys from metainfo
new_dict[b'announce'] = file_data[b"announce"]
new_dict[b'info'] = file_data[b'info']
key_set = set(new_dict[b'info'].keys()) 
unwanted = key_set - wanted_keys #filter for required dictionary keys
for unwanted_key in unwanted: 
    del new_dict[b'info'][unwanted_key]

# hashing value of info key 
bencoded_info = bencoder.encode(new_dict[b'info'])
hash_obj = hashlib.sha1()
hash_data = bencoded_info
hash_obj.update(hash_data)

print(hash_obj.hexdigest())

