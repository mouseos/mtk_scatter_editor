import sys
import re
import pprint
from tabulate import tabulate
if len(sys.argv) < 2:
	print("Usage: python script.py filename")
	sys.exit(1)

filename = sys.argv[1]
outname = sys.argv[2]
scatter=[]
tmp={}
partindex=0
config=""
first_part=0#最初のパーティションを読み込んだか
try:
	with open(filename, 'r') as file:
		contents = file.readlines()

		for content in contents:
			content=re.sub("\n","",content)
			if(len(tmp) != 0 and "- partition_index" in content):
				scatter.append(tmp)
				tmp={}
				first_part=1
			if("- partition_index" in content):
				partindex=1
				tmp[re.sub("- | ","",content.split(":")[0])] = content.split(":")[1]
				first_part=1
			if(first_part == 0):
				config+=content+"\n"
			elif(":" in content and partindex==1):
				value=re.sub(" ","",content.split(":")[1])
				if("0x" in value):
					value=int(value, 16)
				tmp[re.sub(" ","",content.split(":")[0])] = value
		scatter.append(tmp)
		pprint.pprint(scatter)
	
	cnt=0
	table=[]
	head=["番号","名前","開始(B)","終了(B)","サイズ(B)","サイズ(最適化)"]
	for data in scatter:
		partition_size = data["partition_size"]
		if partition_size >= 1024*1024*1024:
			# Convert to GB
			partition_size = str(partition_size / (1024*1024*1024))+"GB"
		elif partition_size >= 1024*1024:
			# Convert to MB
			partition_size = str(partition_size / (1024*1024))+"MB"
		else:
			# Convert to KB
			partition_size = str(partition_size / 1024)+"KB"
		table.append([cnt,data["partition_name"],(data["linear_start_addr"]),(data["linear_start_addr"]+data["partition_size"]),(data["partition_size"]),partition_size])
		cnt+=1
	print(tabulate(table, headers=head, tablefmt="grid"))
	print("パーティション番号：", end="")
	while(True):
		part_num=int(input())
		#パーティション存在確認
		if(part_num in range(len(table))):
			break
		else:
			print("存在するパーティション番号を指定してください。")
	print("拡張:1\n縮小:2")
	print("選択：", end="")
	while(True):
		option=int(input())
		if((option) in [1,2]):
			break
		else:
			print("正しい値を入力してください。")
	
	if(option ==1 or option==2):
		while(True):
			print("サイズを入力してください(例：120 100K 10M 2G)")
			print("サイズ：", end="")
			size=input()
			if("k" in size or "K" in size):
				size=int(''.join(filter(str.isdigit, size)))*1024
			elif("m" in size or "M" in size):
				size=int(''.join(filter(str.isdigit, size)))*1024*1024
			elif("g" in size or "G" in size):
				size=int(''.join(filter(str.isdigit, size)))*1024*1024*1024
			else:
				size=int(size)
			
			if(option==2 and size>=scatter[part_num]["partition_size"]):
				print("縮小サイズが大きすぎます。")
			else:
				break;
		#サイズ編集
		for i in range(part_num,len(scatter)):
			print(scatter[i]["partition_name"]+"を処理中")
			if(i==part_num):
				if(option==1):
					scatter[i]["partition_size"]+=size
				else:
					scatter[i]["partition_size"]-=size
			else:
				if(option==1):
					scatter[i]["linear_start_addr"]+=size
					scatter[i]["physical_start_addr"]+=size
				else:
					scatter[i]["linear_start_addr"]-=size
					scatter[i]["physical_start_addr"]-=size
		
		
		#ファイル生成
		save_txt=config
		for line in scatter:
			cnt=0
			for key, value in line.items():
				if(type(value) is int):
					value=hex(value)
				if(cnt!=0 and cnt!=1):
					save_txt+=("  "+f"{key}: {value}"+"\n")
				elif(cnt==0):
					save_txt+=("\n- "+f"{key}: {value}"+"\n")
				cnt+=1
		print(save_txt)
		with open(outname, 'w') as f:
			print(f.write(save_txt))
except FileNotFoundError:
	print(f"Error: file '{filename}' not found.")
