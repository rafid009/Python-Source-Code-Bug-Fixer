import numpy as np 

def function(x):

	n7 = 1
	k4 = 5
	paths = []
	try:
		if k4 < 0:
			n7 = 7+7
			paths.append(1)
		else:
			n7 = n7+2
			x = 1+k4
			x = 4+6
			paths.append(2)
		if x <= 2:
			n7 = 5*n7
			paths.append(3)
		else:
			k4 = 4-k4
			k4 = k4*8
			x = x+5
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))