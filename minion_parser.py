# Irfansha Shaik, Swansea, 25.05.2019
# Minion data parser
# Input: minion raw data
# Output: R format of the data
# example usage: python minion_parser.py [input_file_path] > [output_file_path]

import sys

with open(sys.argv[1]) as file:
  lines = file.readlines()
  print("N t nds sol")
  N = 0
  for line in lines:
    div_lines = line.rstrip("\n").split(":")
    if (div_lines[0] == "Total Wall Time"):
      N = N + 1
      print (N),
      print (div_lines[1].lstrip(" ")),
    if (div_lines[0] == "Total Nodes"):
      print (div_lines[1].lstrip(" ")),
    if (div_lines[0] == "Solutions Found"):
      print (div_lines[1].lstrip(" "))
