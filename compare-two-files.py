from difflib import SequenceMatcher

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

file1 = open("downloaded.txt")
file2 = open("torrents.txt")
file3 = open("output.txt", 'w')

for line1 in file1:	
	file2.seek(0)
	for line2 in file2:			
			#if line1.lower() == line2.lower():				
			if similar(line1.lower(), line2.lower()) >= 0.8:				
				file3.write(line1)				
				break				

file1.close()
file2.close()
file3.close()
