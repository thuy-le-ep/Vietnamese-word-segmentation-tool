import os
import io
import time
import glob
import shutil
from collections import Counter

# fuction run tool and get time excute
def runTool(cmd):
	start = time.time()
	os.system(cmd)
	return time.time() - start

# function tinh do chinh xac trung binh
FJoin = os.path.join
def GetFiles(path):
    file_list = []
    for dir, subdirs, files in os.walk(path):
        file_list.extend([FJoin(dir, f) for f in files])
    return file_list

def calAcc(folder):
	files = GetFiles(os.path.expanduser(folder))
	accArr = list()
	# Đối với mỗi file kết quả của vnTokenizer, mở file kết quả chuẩn
	# So sánh xem có bao nhiêu từ giống nhau
	# acc = số từ giống / tổng số từ
	for file in files:
		f = io.open(file, 'r', encoding='utf8')
		outputVntokenizer = f.read().split()
		fileOutput = 'Output/' + (file.split('\\')[1]).split('.')[0] +'.txt'
		f.close()

		f2 = io.open(fileOutput, 'r', encoding='utf8')
		out = f2.read().split()
		f2.close()

		diff = Counter(out) - Counter(outputVntokenizer)
		acc = (len(out)-len(list(diff.elements())))/len(out)
		accArr.append(acc)

	accAvg = sum(accArr)/float(len(accArr))
	return accAvg

# function ghi kết quả vào file
def writeFile(content, fileName):	
	f = io.open(fileName, 'w', encoding='utf8')
	f.write(content)
	f.close()

# function copy file 
def copyFile(source_dir, dest_dir, extension):
	files = glob.iglob(os.path.join(source_dir, extension))
	for file in files:
		if os.path.isfile(file):
			shutil.copy2(file, dest_dir)

# start
def myTestcase():
	# vntokenizer
	timeVntokenizer = runTool('cd vnTokenizer && java -jar vn.hus.nlp.tokenizer-4.1.1.jar -i Input -o Output -e .txt')
	copyFile(r'vnTokenizer/Output', r'OutputvnTokenizer', '*.txt')
	accVntokenizer = calAcc(r"OutputvnTokenizer")

	# jvntextpro
	timeJvntextpro = runTool('cd JVnTextpro && java -cp bin;libs/args4j.jar;libs/lbfgs.jar jvnsegmenter.WordSegmenting -modeldir models\jvnsegmenter -inputdir Input')
	copyFile(r'JVnTextpro/Input', r'OutputJVnTextpro', '*.wseg')
	accJvntextpro = calAcc(r"OutputJVnTextpro")

	# dongdu
	timeDongdu = runTool('cd Dongdu && dongdu.exe -i Input -o Output')
	copyFile(r'Dongdu/Output', r'OutputDongdu', '*.txt')
	accDongdu = calAcc(r"OutputDongdu")

	# ketqua
	content = \
		'Kết quả:\n' +\
		'	- vnTokenizer\n' +\
		'		- time: ' + str(timeVntokenizer) +'\n' +\
		'		- acc: ' + str(accVntokenizer) +'\n' +\
		'	- JVnTextpro\n' +\
		'		- time: ' + str(timeJvntextpro) +'\n' +\
		'		- acc: ' + str(accJvntextpro) +'\n' +\
		'	- Dongdu\n' +\
		'		- time: ' + str(timeDongdu) +'\n' +\
		'		- acc: ' + str(accDongdu) +''

	writeFile(content,'ketqua.txt')

myTestcase()
