# Irfansha Shaik, 17.05.2020, Aarhus.

import sys
import subprocess
import re

# Generate R file:
def export_R(data, output_fp):
	f = open(output_fp, "w")
	# We only consider input size, node count, solution count and time:
	header = "N nds sol t \n"
	f.write(header)
	for k, v in data.items():
		data_line = str(k) + " " + v[6] + " " + v[8] + " " + v[0] + "\n"
		f.write(data_line)

# collects nqueens data:
def collect(filepath, data):
	N = 0
	f = open(filepath, 'r')
	lines = f.readlines()
	data_list = []
	# Getting the N from file name:
	m = re.search('n_queens_(.+?).param.info',filepath)
        if m:
		N = int(m.group(1))
	# Listing the stats:
	for line in lines:
		line = line.strip("\n")
		temp = line.split(":")
		data_list.append(temp[1])
	data[N] = data_list

# Takes path of the datafiles folder produced by savilerow:
def main(argv):
	datafiles_dirpath = sys.argv[1]
	output_fp = sys.argv[2]
	data = {}
	proc = subprocess.Popen(["ls " + datafiles_dirpath + "/*.info"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
        files_list = out.split("\n")
	# now collecting data from each file:
        for datafile in files_list:
		if len(datafile) != 0:
			collect(datafile, data)
	export_R(data,output_fp)
	#print(data)
if __name__ == "__main__":
	main(sys.argv[1:])
