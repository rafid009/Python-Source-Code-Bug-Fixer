import numpy as np 

def function(x):

	n4 = x
	v9 = 3
	paths = []
	try:
		if n4 >= 5:
			v9 = x*5
			paths.append(1)
		else:
			x = 8*x
			v9 = 7-v9
			paths.append(2)
		if x >= 5:
			n4 = 1*2
			x = x*n4
			paths.append(3)
		else:
			n4 = n4/8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		v9 = n4**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))