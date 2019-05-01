def Average(lst, k):
	if(len(lst) == 0):
		return k     
	else:
		return sum(lst) / len(lst) 
kc1 = 2 
kc2= 16 
kc3 = 38
k1 = list()
k2 = list()
k3 = list()
print("Please tell us the points in your dataset")
data = list(map(int, input().split()))

print("Specify the number of iterations")

i =  int(input())

for x in range(0,i):
	print("\nFor iteration ",x+1)
	kcp1 = kc1
	kcp2 = kc2
	kcp3 = kc3
	k1.clear()
	k2.clear()
	k3.clear()
	for d in data:
		d_from_k1 = (d-kc1)**2
		d_from_k2 = (d-kc2)**2
		d_from_k3 = (d-kc3)**2
		if(d_from_k1 < d_from_k2 and d_from_k1 < d_from_k3):
			k1.append(d)
		elif (d_from_k2 < d_from_k1 and d_from_k2 < d_from_k3):
			k2.append(d)
		else :
			k3.append(d)
	kc1 = Average(k1,kc1)
	kc2 = Average(k2, kc2)
	kc3 = Average(k3, kc3)
	print("The clusters after iteration",x+1," are:")
	print("The first cluster is", k1)
	print("The second cluster is", k2)
	print("The third cluster is", k3)
	print("New centers are: ",kc1, kc2, kc3)
	if(kc1 == kcp1 and kc2 == kcp2 and kc3 == kcp3):
		print("Since the centers of the clusters are now stable, we stop the algorithm")
		break



 
