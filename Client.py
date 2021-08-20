import sys
import bencoder
import hashlib

file_in = sys.argv[1] # take torrent as input from command line
torrent = open(f'C:/Users/Mister Gardner/Desktop/BitTorrent client project/{file_in}', 'rb')

file_data = bencoder.decode(torrent.read()) #decode bencoded torrent file
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
hash_obj = hashlib.sha1()
hash_data = str(new_dict[b'info'])
hash_obj.update(hash_data.encode())

print(hash_obj.digest())

