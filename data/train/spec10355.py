import numpy as np 

def function(x):

	k8 = 3
	j3 = 6
	paths = []
	try:
		if k8 > 0:
			j3 = x/2
			j3 = k8-j3
			paths.append(1)
		else:
			j3 = j3*1
			paths.append(2)
		if j3 < 3:
			x = x/k8
			x = 7+2
			x = x+4
			paths.append(3)
		else:
			k8 = 6-k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))