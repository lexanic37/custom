import socket
prefixs = ['','.ad.ing.net','.ru.ing.net', '.europe.intranet', '.srv.pl.ING.NET']
domains = open('domains','r')
result = {}



for line in domains:
	if 'net' not in line:
		for prefix in prefixs:
			ip=''
			print(line.strip() + prefix)
			try:
				domain = line.strip() + prefix
				ip = socket.gethostbyname(domain)
				print(domain)
				print(ip)
				

			except:
				print("net")
			file = open('resolved_domains','a')
			if ip !='':
				result = domain + ':'+ ip
				print(result)
				file.write(domain + ':'+ ip +'\n')	
			else:
				file.write(domain + ': Not resolve\n')

			file.close()