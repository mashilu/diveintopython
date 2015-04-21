import os
import sys
try:
	from UserDict import UserDict
except:
	from collections import UserDict

def stripnulls(data):
	"strip whitespace and nulls"
	return data.replace("\00", "").strip()

class FileInfo(UserDict):
	"store file metadata"
	def __init__(self, filename=None):
		UserDict.__init__(self)
		self["name"] = filename

class MP3FileInfo(FileInfo):
	"store ID3v1.0 MP3 tags"
	tagDataMap = {"title"	: (3, 33, stripnulls),
				  "artist"	: (33, 63, stripnulls),
				  "album"	: (63, 93, stripnulls),
				  "year"	: (93, 97, stripnulls),
				  "comment"	: (97, 126, stripnulls),
				  "genre"	: (127, 128, ord)}

#	print(tagDataMap.items())
	def __parse(self, filename):
		"parse ID3v1.0 tags from MP3 file"
		self.clear()
		try:
			print(filename)
			fsock = open(filename, "rb", 0)
			try:
				fsock.seek(-128, 2)
				tagdata = fsock.read(128)
			finally:
				fsock.close()
			print(tagdata[:3])
			if tagdata[:3].decode("gbk") == "TAG":
				print("Asdf")
				for tag, (start, end, parseFunc) in self.tagDataMap.items():
					print(tag)
					self[tag] = parseFunc(tagdata[start:end].decode("gbk"))
		except IOError:
			print("*****")
			pass

	def __setitem__(self, key, item):
		if key == "name" and item:
			self.__parse(item)
		FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):
	"get list of file info objects for files of particular extensions"
	fileList = [os.path.normcase(f)
				for f in os.listdir(directory)]
	fileList = [os.path.join(directory, f)
				for f in fileList
				if os.path.splitext(f)[1] in fileExtList]
	def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
		"get file info class from filename extension"
		subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
		return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
	return [getFileInfoClass(f)(f) for f in fileList]

if __name__ == "__main__":
	for info in listDirectory("/Users/apple/Desktop", [".mp3"]):
		print("\n".join(["%s = %s" % (k, v) for k, v in info.items()]))

