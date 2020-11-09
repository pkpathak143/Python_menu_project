import os
import getpass

os.system("tput setaf 2")
print("\n\n\n\t-----------------------------------------------------------------------------------------")

os.system("tput setaf 4")
print("\t\t\t\tW E L C O M E   T O   T H E   P R O J E C T ")

os.system("tput setaf 2")
print("\t-----------------------------------------------------------------------------------------\n\n")

os.system("tput setaf 1")
passwd = getpass.getpass("Enter your password : ")

apasswd = "redhat"

if passwd != apasswd:
	print("Incorrect Password!!")
	os.system("tput setaf 7")
	exit()

os.system("tput setaf 3")
print("Where do you want to perform your Job (local/remote) :", end=" ")
location=input()

print(location)

if location == 'remote':
	remoteIP = input("Enter the IP address : ")

while True:
	os.system("tput setaf 7")
	print("""
	Press 1: to see date
	Press 2: to check calender 
	Press 3: Configure the web server
	Press 4: to create user
	Press 5: to create a folder
	Press 6: to setup hadoop
	Press 7: to setup Docker
	Press 8: to exit
	""")

	print("Enter your choice: ", end=" ")

	ch=input()
	print(ch)

	if location == 'local':

		if int(ch) == 1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			print("""
	Press 1: to install httpd
	Press 2: to upload the file
	Press 3: to start the services
	Press 4: to stop the services
			""")
			choice = input("Enter your choice: ")
			if int(choice) == 1:
			    confg = input("yum configured?(y/N)")
			    if confg == 'y':
			        os.system("yum install httpd")
			    elif confg == 'N':
			        print("Please configure yum first")
			    else:
			        print("Invalid Input!!")
			elif int(choice) == 2:
			    fname = input("Just write the file name if it is there where you have run this program or write the complete path \n(eg: /root/dir1/file1.html) : ")
			    os.system("cp {} /var/www/html ".format(fname))
			    print("---File-copied---")
			elif int(choice) == 3:
			    os.system("systemctl start httpd")
			elif int(choice) == 4:
			    os.system("systemctl stop httpd")
			else:
			    print("Invalid Input!!")
		elif int(ch) == 4:
			print("What user name you want to give?")
			create_user = input()
			os.system("useradd {}".format(create_user))
		elif int(ch) == 5:
			dirname = input("Name of the folder you want to give:")
			os.system("mkdir {}".format(dirname))
		elif int(ch) == 6:
			print('''
	Press 1: to Setup Master
	Press 2: to Setup Slave
	Press 3: to Setup Client
	Press 4: to read a manual of Hadoop Cluster
			''')
			print("Enter your choice: ", end=" ")
			choice=input()
			print(choice)
			if int(choice) == 1:
				confm = input("Master Configured?(y/N):")
				if confm == "y":
					print("Press 1: to Start: \nPress 2: to Stop: \nPress 3: to see the statistics of the cluster: ")
					opt1 = input("Enter your option: ")
					if int(opt1) == 1:
						os.system("hadoop-daemon.sh start namenode")
						print("----NameNode-Started----")
						os.system("jps")
					elif int(opt1) == 2:
						os.system("hadoop-daemon.sh stop namenode")
						print("----NameNode-Stopped----")
						os.system("jps")
					elif int(opt1) == 3:
						print("----Welcome-to-the-Cluster----")
						os.system("hadoop dfsadmin -report")
					else:
						print("Invalid Input!!")
				elif confm == "N":
					print("--Read-the-Manual-of-Hadoop-Cluster--")
				else:
					print("Invalid Input!!")
			elif int(choice) == 2:
				confs = input("Slave Configured?(y/N)")
				if confs == "y":
					print("Press 1: to Start: \nPress 2: to Stop: \nPress 3: to see the statistics of the cluster: ")
					opt1 = input("Enter your option: ")
					if int(opt1) == 1:
						os.system("hadoop-daemon.sh start datanode")
						print("----DataNode-Started----")
						os.system("jps")
					elif int(opt1) == 2:
						os.system("hadoop-daemon.sh stop datanode")
						print("----DataNode-Stopped----")
						os.system("jps")
					elif int(opt1) == 3:
						print("----Welcome-to-the-Cluster----")
						os.system("hadoop dfsadmin -report")
					else:
						print("Invalid Input!!")
				elif confs == "N":
					print("--Read-the-Manual-of-Hadoop-Cluster--")
				else:
					print("Invalid Input!!")
			elif int(choice) == 3:
				confc = input("Client Configured?(y/N):")
				if confc == "y":
					print("""
	Press 1: to see the statistics of the cluster
	Press 2: to list all the files
	Press 3: to upload a file
	Press 4: to read a file
	Press 5: to remove a file
	Press 6: to upload a file with a default value of blocksize
					""")
					opt1 = input("Enter your option: ")
					if int(opt1) == 1:
						print("----Welcome-to-the-Cluster----")
						os.system("hadoop dfsadmin -report")
					elif int(opt1) == 2:
						print("----Welcome-to-the-Cluster----")
						os.system("hadoop fs -ls /")
					elif int(opt1) == 3:
						print("----Welcome-to-the-Cluster----")
						file_name = input("Enter the file name which you want to upload:")
						os.system("hadoop fs -put {} /".format(file_name))
						print("----File-Uploaded----")
					elif int(opt1) == 4:
						print("----Welcome-to-the-Cluster----")
						file_name = input("Enter the file name which you want to read:")
						os.system("hadoop fs -cat /{}".format(file_name))
						print("----File-Viewed----")
					elif int(opt1) == 5:
						print("----Welcome-to-the-Cluster----")
						file_name = input("Enter the file name which you want to remove:")
						os.system("hadoop fs -rm /{}".format(file_name))
						print("----File-Removed----")
					elif int(opt1) == 6:
						print("----Welcome-to-the-Cluster----")
						file_name = input("Enter the file name which you want to upload:")
						block_size = input("Enter the block size in bytes (Hint: 1 MB = 1048576 Bytes) :")
						os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(block_size,file_name))
						print("----File-Uploaded----")
					else:
						print("Invalid Input!!")
				elif confc == "N":
					print("--Read-the-Manual-of-Hadoop-Cluster--")
				else:
					print("Invalid Input!!")
			elif int(choice) == 4:
				print("""

	\tHADOOP CONFIGURATION FOR NAME NODE(MASTER)
	\t  ~- ASSUMING HADOOP IS PREINSTALLED -~

	Step 1 : Go to core-site.xml file using bellow command:
	cd vim /etc/hadoop/core-site.xml

	Step 2 : Write the following statements in the coresite.xml file

	<property>
	<name>fs.default.name</name>
	<value>hdfs://master-ip:9001</value>
	</property>

	Step 3 : Go to hdfs-site.xml file using bellow command:
	vim /etc/hadoop/hdfs-site.xml

	Step 4 : Write the following statements in hdfs-site.xml file

	<property>
	<name>dfs.name.dir</name>
	<value>/nn1</value>
	</property>



	\tHADOOP CONFIGURATION FOR DATA NODE(SLAVE)
	\t  ~- ASSUMING HADOOP IS PREINSTALLED -~

	Step 1 : Go to core-site.xml file using bellow command:
	cd vim /etc/hadoop/core-site.xml

	Step 2 : Write the following statements in the coresite.xml file

	<property>
	<name>fs.default.name</name>
	<value>hdfs://master-ip:9001</value>
	</property>

	Step 3 : Go to hdfs-site.xml file using bellow command:
	vim /etc/hadoop/hdfs-site.xml

	Step 4 : Write the following statements in hdfs-site.xml file

	<property>
	<name>dfs.data.dir</name>
	<value>/dn1</value>
	</property>



	\t   HADOOP CONFIGURATION FOR CLIENT
	\t -~ASSUMING HADOOP IS PREINSTALLED~-

	Step 1 : Go to core-site.xml file using bellow command:
	cd vim /etc/hadoop/core-site.xml

	Step 2 : Write the following statements in the coresite.xml file

	<property>
	<name>fs.default.name</name>
	<value>hdfs://master-ip:9001</value>
	</property>



	\t COMMANDS THAT CAN BE USED BY CLIENTS

	hadoop fs -ls / ---> to see the files in cluster

	hadoop fs -put [filename] / ---> to upload the files in cluster

	hadoop fs -rm /[filename] ---> to remove the files from the cluster

	hadoop fs -cat /[filename] ---> to read the files from the cluster

	hadoop fs -Ddfs.block.size=64M - put [filename] / ---> to upload the file with blocksize
				""")
			else:
				print("Invalid Input!!")
			
		elif int(ch) == 7:
			print("""
	Press 1: to check version
	Press 2: to list the running containers
	Press 3: to list all the containers
	Press 4: to list images
	Press 5: to download image
	Press 6: to launch new container
	Press 7: to pause the running container
	Press 8: to unpause the container
	Press 9: to start the stopped container
	Press 10: to stop the container 
	Press 11: to attach the started container
	Press 12: to remove the container
	Press 13: to remove the image
	Press 14: to upload the image on Docker Hub
	Press 15: to check the logs
			""")
			op = input("choose your option: ")
			if int(op) == 1:
			    os.system("docker version")

			elif int(op) == 2:
			    os.system("docker ps")

			elif int(op) == 3:
			    os.system("docker ps -a")

			elif int(op) == 4:
			    os.system("docker images")

			elif int(op) == 5:
			    opt1 = input("Enter the image name (eg: centos,ubuntu) : ")
			    os.system("docker pull {}".format(opt1))
			elif int(op) == 6:
			    opt1 = input("Please enter the image name  \n(eg: centos:latest) : ")
			    opt2 = input("Enter a specific name if you want to name it :")
			    os.system("docker run -it --name={}  {}".format(opt2,opt1))

			elif int(op) == 7:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker pause {}".format(opt1))

			elif int(op) == 8:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker unpause {}".format(opt1))

			elif int(op) == 9:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker start {}".format(opt1))

			elif int(op) == 10:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker stop {}".format(opt1))

			elif int(op) == 11:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker attach {}".format(opt1))

			elif int(op) == 12:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker rm {}".format(opt1))

			elif int(op) == 13:
			    opt1 = input("Please enter the image name : ")
			    os.system("docker rmi {}".format(opt1))

			elif int(op) == 14:
			    opt1 = input("Please enter the image name : ")
			    os.system("docker push {}".format(opt1))

			elif int(op) == 15:
			    opt1 = input("Please enter the container name : ")
			    os.system("docker logs {}".format(opt1))

			else:
			    print("Invalid Input!!")

		elif int(ch) == 8:
			os.system("tput setaf 2")
			print("\t-----------------------------------------------------------------------------------------")
			print("\t\t\t\t\tT H A N K - Y O U ! !")
			print("\t-----------------------------------------------------------------------------------------\n\n")
			os.system("tput setaf 7")
			exit()

		else:
			print("option not supported")
		input("\n\n Press ENTER to continue......")
		os.system("clear")
	
	elif location == 'remote':
		"""
		if int(ch) == 1:
			os.system("ssh {} date".format(remoteIP))
		elif int(ch) == 2:
			os.system("ssh {} cal".format(remoteIP))
		elif int(ch) == 3:
			os.system("abc")
		elif int(ch) == 4:
			print("What user name you want to give?")
			create_user = input()
			os.system("ssh {} useradd {}".format(remoteIP, create_user))
		elif int(ch) == 5:
			os.system("ssh {} date".format(remoteIP))
		elif int(ch) == 6:
			os.system("ssh {} date".format(remoteIP))
		elif int(ch) == 7:
			exit()
		elif int(ch) == 8:
			exit()
		else:
			print("option not supported")
		"""
		
	else:
		print("Location dosen't support")


os.system("tput setaf 7")


