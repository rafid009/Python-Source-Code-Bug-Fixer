import numpy as np 

def function(x):

	k1 = 9
	n9 = x
	paths = []
	try:
		if k1 < 2:
			x = 4-x
			paths.append(1)
		else:
			x = k1*1
			k1 = 3/k1
			n9 = x/k1
			paths.append(2)
		if k1 > 6:
			n9 = 9-3
			x = 6+8
			paths.append(3)
		else:
			k1 = k1/5
			n9 = 7-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))