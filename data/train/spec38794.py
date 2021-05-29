import numpy as np 

def function(x):

	n0 = x
	k3 = 8
	paths = []
	try:
		if x > 9:
			n0 = n0*2
			k3 = 6-n0
			paths.append(1)
		else:
			k3 = k3*9
			n0 = n0-k3
			k3 = 4+k3
			paths.append(2)
		if n0 <= 9:
			n0 = 1*n0
			paths.append(3)
		else:
			k3 = n0/7
			x = 2-x
			x = 4/4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		k3 = n0**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))