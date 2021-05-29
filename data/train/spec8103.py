import numpy as np 

def function(x):

	k4 = x
	n6 = x
	paths = []
	try:
		if n6 < 2:
			k4 = k4-9
			k4 = 3+4
			k4 = x/7
			paths.append(1)
		else:
			k4 = k4-2
			k4 = k4*7
			k4 = k4+1
			paths.append(2)
		if n6 >= 1:
			k4 = k4/9
			k4 = k4+5
			paths.append(3)
		else:
			k4 = 8*8
			k4 = x*n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))