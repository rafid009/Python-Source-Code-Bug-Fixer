import numpy as np 

def function(x):

	n8 = x
	k1 = 0
	paths = []
	try:
		if n8 >= 8:
			k1 = 4*k1
			k1 = 3-n8
			n8 = 9-0
			paths.append(1)
		else:
			x = k1/x
			x = n8-x
			paths.append(2)
		if k1 < 1:
			n8 = 2+n8
			n8 = 5+3
			k1 = k1*7
			paths.append(3)
		else:
			k1 = 4*k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))