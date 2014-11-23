#! /usr/bin/env python3

# Name: AwesomeGroupList 
#
# Version: 0.0.1
#
# Author: Sinuhe Jaime Valencia
#
# Author_email: sierisimo@gmail.com
#
# Description: 
#     Main file for AwesomeGroupLists
#

if __name__ == "__main__":
	while True:
		data = input("Give a url:")

		if (not "http://" in data) and (not "https://" in data):
			print("Please give a valid url.",end="\n\n")
			continue
		
		size_split = len(data.split("."))
		if size_split < 2:
			print("Really, please, give a valid url.")
			continue

		last_part = data.split("/")[-1]
		video_code = last_part.split("/")
		
		parte_chida = video_code[0].split("=")
		print(parte_chida[1])