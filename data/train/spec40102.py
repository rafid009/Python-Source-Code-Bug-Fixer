import numpy as np 

def function(x):

	k5 = 7
	n4 = x
	paths = []
	try:
		if k5 >= 4:
			k5 = 6-k5
			n4 = n4-k5
			x = n4/n4
			paths.append(1)
		else:
			k5 = x*x
			x = 7-x
			n4 = 5-n4
			paths.append(2)
		if n4 < 5:
			x = x+x
			k5 = 2-n4
			paths.append(3)
		else:
			x = 6*x
			k5 = k5-x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))