import pandas as pd
import csv, json, random, re
from bs4 import  BeautifulSoup
import codecs
'''
Given a list of strings between <code> </code> tags for a question or answer post, returns the maximum length element in the list. 
We shall consider this to be the major code snippet. Other elements will be discarded.
'''
def findMostImportantCodeSnippet(listOfCodes):
	return max(listOfCodes,key=len)

csvfilename = 'query.csv'
dictfile = 'qid_aid_dict_sampled.json'
SampleSize = 1000 				# Sample 1000 items out of the 50,000 Q&A pairs.
df = pd.read_csv(csvfilename,index_col=0,names=["QId","QBody","AId","ABody"], encoding='utf-8')

rows = random.sample(df.index,SampleSize)
sampled_df = df.ix[rows]

m_qId_aId = {}					#Dictionary to map Q ids and A ids.
for i,row in sampled_df.iterrows():
	try:
		qbody = str(row['QBody'])
		abody = str(row['ABody'])
		qcodes = re.compile('<code>(.*?)</code>', re.DOTALL).findall(qbody)		#Uses regex to find text between <code> and </code> tags
		qcodes = [BeautifulSoup(code).get_text() for code in qcodes]			#Beautifies the text. Replaces classic HTML encoding with regular texts.
		acodes = re.compile('<code>(.*?)</code>', re.DOTALL).findall(abody)
		acodes = [BeautifulSoup(code).get_text() for code in acodes]
		if len(qcodes) != 0 and len(acodes) != 0:				#Ignore Q&A pair with only text and no code
			impQcode = findMostImportantCodeSnippet(qcodes)			#Identify the most useful code snippet for the Question
			impAcode = findMostImportantCodeSnippet(acodes)			#Identify the most useful code snippet for the Answer
				
			#Write the question and answer code snippets to different files, IDed by the QId or AId respectively.
			fp1 = codecs.open("Questions/"+i+".js","w", encoding='utf-8')
			fp1.write(impQcode)
			fp2 = codecs.open("Answers/"+row['AId']+".js","w",encoding='utf-8')
			fp2.write(impAcode)
			m_qId_aId[i] = str(int(row['AId']))
			fp1.close()
			fp2.close()
	except UnicodeEncodeError:
		pass

with open(dictfile,'w') as fp:
	json.dump(m_qId_aId,fp,indent=4)
print("Success")
