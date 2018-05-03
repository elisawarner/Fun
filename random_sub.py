# Takes a random subset of the source file
import pandas as pd
import random as r
import os
import time

# time
start = time.time()

## User Parameters
filename = '/Users/elisawarner/Desktop/Accidents/accident.csv' # source file
export_prefix = '/Users/elisawarner/Desktop/Accidents/Samples/' # output file folder
file_prefix = 'acc' # output file prefix
desired_no_of_records = 500
desired_no_of_files = 10
DELIMITER = ','

################## FOR NORMAL FILES ############################


df = pd.read_csv(filename, header = 0, delimiter = DELIMITER, low_memory = False)
end = time.time()

print("Finished reading file in %d seconds" % (end - start))

for n in range(desired_no_of_files):
	sub_list = []
	start = time.time()
	for i in range(desired_no_of_records):
		random_interval = (r.randint(0,len(df.index)))
		sub_list.append(list(df.as_matrix()[random_interval-1]))

	sub_df = pd.DataFrame(sub_list, columns=list(df))
	sub_df.to_csv(export_prefix + file_prefix + '_%s.csv' % (n), header=True, index=False)
	end = time.time()
	print("Completed %s_%s.csv in %d seconds" % (file_prefix, n, end - start))

print("Copied files:")
os.system('ls %s%s_*.csv' % (export_prefix, file_prefix))


################### FOR IMPOSSIBLY LARGE FILES ##########################
# when you select desired_no_of_files, its desired number per chunk
"""
chunksize = 2 ** 19 #524288
chunk_count = 0
for chunk in pd.read_csv(filename, chunksize=chunksize, delimiter=DELIMITER, error_bad_lines=False):
	for n in range(desired_no_of_files):
		sub_list = []
		start = time.time()
		for i in range(desired_no_of_records):
			random_interval = (r.randint(0,len(chunk.index)))
			sub_list.append(list(chunk.as_matrix()[random_interval-1]))

		sub_df = pd.DataFrame(sub_list, columns=list(chunk))
		sub_df.to_csv(export_prefix + file_prefix + '_%s.csv' % (n + chunk_count), header=True, index=False)
		end = time.time()
		print("Completed %s_%s.csv in %d seconds" % (file_prefix, n + chunk_count, end - start))
	chunk_count += 1


print("Copied files:")
os.system('ls %s%s_*.csv' % (export_prefix, file_prefix))
"""


#### VIEW STUFF ####
"""
os.system('ls /Users/elisawarner/Desktop/Sample_Stuff/SGV_Study_6_*.csv > outfile')

fhnd = open('outfile')
file_list = fhnd.read().split('\n')
fhnd.close()

for i in range(len(file_list)):
	os.system('mv %s /Users/elisawarner/Desktop/Sample_Stuff/estd214_%s.csv' % (file_list[i], i))

os.system('ls /Users/elisawarner/Desktop/Sample_Stuff/*.csv')
"""
