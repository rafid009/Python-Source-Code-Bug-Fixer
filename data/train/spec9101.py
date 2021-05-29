import numpy as np 

def function(x):

	n4 = 6
	k4 = 8
	paths = []
	try:
		if n4 < 7:
			x = x/9
			k4 = x*6
			paths.append(1)
		else:
			x = x+8
			k4 = k4+0
			paths.append(2)
		if x <= 1:
			n4 = 5*x
			k4 = k4+7
			paths.append(3)
		else:
			k4 = 2+k4
			k4 = k4*7
			n4 = n4/9
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))