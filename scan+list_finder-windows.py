import os
def prepare(text):
	text=text.replace("(", "").replace(")", "")
	return text
	
def prepare_ip(text):
	if(text[len(text)-1]!="."):
		text=text[:(len(text)-1)]
	if(text[len(text)-1]!="."):
		text=text[:(len(text)-1)]
	if(text[len(text)-1]!="."):
		text=text[:(len(text)-1)]	
	return text[:-1]

def find_ip_windows():
	ipconfig=os.popen("ipconfig")
	ip_lines=ipconfig.readlines()
	words=ip_lines[-8].split()
	ip=words[-1]
	ip=prepare_ip(ip)
	return ip

def net_scan():
	ip=find_ip_windows()
	scan=os.popen("nmap -sP "+str(ip)+".0/24")
	scan_lines=scan.readlines()
	output_file=open("scan.txt", "w")
	for line in scan_lines:
		output_file.write(line)
	output_file.close()

def adress_list():
	net_scan()
 	input_file=open('scan.txt',"r+")
 	work_file=open('roboczy.txt',"w+")
 	output_file=open('IPs+MACs.txt', "w+")
 	in_lines=input_file.readlines()
 	input_file.close()
 	i=1
 	for line in in_lines:
 		if(i>2 and i%3!=1):
 			work_file.write(line)
 		i+=1
 	i=1
 	work_file.close()
 	work_file=open('roboczy.txt',"r+")
 	work_lines=work_file.readlines()
 	work_file.close()
 	for line in work_lines:	
 		words=line.split()
 		if(i%2==1):
 			output_file.write(prepare(words[-1])+"\t")
 		else:
 			output_file.write(prepare(words[2])+"\n")
 		i+=1
 	output_file.close()
 	os.remove('roboczy.txt')
	
adress_list() 
ip=find_ip_windows()
print ip
