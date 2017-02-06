import scipy.io
import sys
def cournot(m1, m2, a1, a2, N):
	prev = [a1[0][0]-1, a2[0][0]-1]
	
	print("Initial: [" + str(prev[0]) + ", " + str(prev[1]) + "]")
	for i in range(0,N[0][0]):
		# check if player 1 wants to change
		prevp2 = prev[1]
		prevp1 = prev[0]
		newp1 = prev[0]
		newp2 = prev[1]
		if i % 2 == 0:
			for k in range(0,len(m1)):
				if m1[k][prevp2] > m1[newp1][prevp2]:
					newp1 = k
		# check if player 2 wants to change
		elif i % 2 == 1:
			for k in range(0,len(m2[prevp1])):
				if m2[prevp1][k] > m2[prevp1][newp2]:
					newp2 = k
		prev = [newp1, newp2]
		print("Stage " + str(i) + ": [" + str(newp1) + ", " + str(newp2) + "]")
		
def loadmat(filename):
	return scipy.io.loadmat(filename)
		
def main(filename):
	print("Using: " + filename)
	try:
		p1 = loadmat(filename)
	except:
		print("Error opening file " + str(filename))
		exit()
	cournot(p1["M1"], p1["M2"], p1["a1"], p1["a2"], p1["n"])
	return

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python cournot.py (filename)")
	main(sys.argv[1])
