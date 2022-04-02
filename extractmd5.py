import hashlib
import glob 

filenames = glob.glob("*.*")
for filename in filenames:
	with open(filename, 'rb') as file:
		data = file.read()
		text= "filename: " + filename + ",  md5: " + hashlib.md5(data).hexdigest()
		print(text)

def md5(file_name):
	hash_md5 = hashlib.md5()
	with open(file_name, "rb") as file:
		for i in iter(lambda: file.read(2 ** 20), b""):
			hash_md5.update(i)
	return hash_md5.hexdigest()
