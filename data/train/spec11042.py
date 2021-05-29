import numpy as np 

def function(x):

	n0 = x
	k1 = 3
	paths = []
	try:
		if k1 < 4:
			k1 = k1+1
			k1 = k1+4
			paths.append(1)
		else:
			n0 = 7*8
			x = 4-5
			k1 = n0/6
			paths.append(2)
		if k1 >= 2:
			n0 = 8+n0
			n0 = 3/n0
			paths.append(3)
		else:
			x = x/7
			x = 8*4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		k1 = n0**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))