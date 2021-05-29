import numpy as np 

def function(x):

	n4 = x
	x6 = 0
	paths = []
	try:
		if n4 < 0:
			x6 = x6/4
			x = 4/x
			paths.append(1)
		else:
			x6 = x/7
			n4 = n4-n4
			n4 = 8/x6
			paths.append(2)
		if x6 <= 0:
			x = 7*5
			n4 = x/n4
			paths.append(3)
		else:
			n4 = n4*n4
			n4 = n4*x6
			x = x6+x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x6 = n4**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))