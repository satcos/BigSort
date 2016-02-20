def big_sort(workDirectory, fileName, splitSize):
	# Open the file for reading
	inFile = open(workDirectory + "\\" + fileName, 'r', encoding="utf8")
	
	# Number of temporary file created
	fileCount = 0
	# Records read in current batch
	recordCount = 0
	# Temporary storage
	tempRecords = []
	
	# Read one line at a time
	for line in inFile:
		# Append it to the temporary storage
		tempRecords.append(line)
		recordCount += 1
		
		# if the size of temporary storage reaches split size
		# sort and write it to a file
		if recordCount == splitSize:
			# Sort temporary file
			tempRecords.sort()
			
			# Open file for writing
			outFile = open(workDirectory + '\\File' + str(fileCount) + '.txt', 'w', encoding="utf8")
			
			# Write one line at a time
			for record in tempRecords:
				outFile.write(record)
			
			# Close the file
			outFile.close()
			
			# Reset the variables
			tempRecords = []
			fileCount += 1
			recordCount = 0
			print("Created split file : ", fileCount)
	
	# Sort and write end of the file content which is less than splitSize
	outFile = open(workDirectory + '\\File' + str(fileCount) + '.txt', 'w', encoding="utf8")
	tempRecords.sort()
	for record in tempRecords:
		outFile.write(record)
	outFile.close()
	# Increment the file count
	fileCount += 1
	print("Created split file : ", fileCount)
	# Close the input file
	inFile.close()
	
	# Now merge the individually sorted files
	big_merge(workDirectory, fileName, fileCount)
	
def big_merge(workDirectory, fileName, totalFileCount):
	print("Merging the split files")
	import heapq
	
	# Input file list
	inFiles = []
	for fileCount in range(totalFileCount):
		inFiles.append(open(workDirectory + '\\File' + str(fileCount) + '.txt', 'r', encoding="utf8"))
	
	# Merge and Write sorted information
	with open(workDirectory + "\\Sorted " + fileName, 'w', encoding="utf8") as out:
		out.writelines(heapq.merge(*inFiles))
	
	# Close the file pointers
	out.close()
	for fileCount in range(totalFileCount):
		inFiles[fileCount].close()

# =============================================================================
# Executing of the script starts here
# Note down the time
import time
start_time = time.time()

# Specify the directory where the big files resides
# In windows escape back slash with back slash
workDirectory = "D:\\MyBigFiles"
# Name of the file to be sorted
fileName = "eventLog.txt"
# Number of lines to retain in each split file
# This need to be varied based on available system RAM
# Lower the RAM less this number should be
splitSize = 5000000

# Sort the file
big_sort(workDirectory, fileName, splitSize)
print("Sorting successfully completed")
print("Total Time Take: ", time.time() - start_time, " seconds")
# =============================================================================