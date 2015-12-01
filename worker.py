import os,json
import matplotlib.pyplot as plt
fp = open('testset','r')
map_target_parent={}
for line in fp:
	target,parent = line.split(',')
	map_target_parent[target] = parent

map_target_threshold={}
map_threshold_count = {}
for k,v in map_target_parent:
	for t in range(30,1,-2):
		if k not in map_target_threshold:
			os.system("jsinspect -t "+str(t)+" --ignore "+k+" ./Questions")
			fp = open(r'*.json',"r")
			outputdata = json.load(fp)
			for filenames in outputdata["instances"]:
				if v in filenames["path"]:
					map_target_threshold[k] = t
		else:
			break

for k,v in map_target_threshold:
	if v in map_threshold_count:
		map_threshold_count[v] += 1
	else
		map_threshold_count[v] = 1

plt.plot(map_threshold_count.keys(),map_threshold_count.values())
plt.ylabel('Count')
plt.xlabel('First discovery threshold')
plt.savefig('output.png')
