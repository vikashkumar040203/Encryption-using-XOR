import random
import string
n = 16
with open('xorfile.txt') as fp:
	line  = fp.readline()
	key  = ''.join(random.choices(string.ascii_lowercase, k=16))
	out = [(line[i:i+n]) for i in range(0, len(line), n)]
	for i in out:
    		# print(newLine)
		xored = [chr(ord(a) ^ ord(b)) for a,b in zip(i, key)]
		finalXored = "".join(xored)
		with open('outputxor.txt','a') as outfp:
			outfp.write(f"{finalXored}\n",)
		# print("XoredList: ",xored)
		print("FinalXored: ",finalXored)