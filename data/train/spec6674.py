import numpy as np 

def function(x):

	l3 = 6
	v7 = 2
	paths = []
	try:
		if l3 <= 6:
			x = x-l3
			paths.append(1)
		else:
			x = 1/x
			v7 = 6-0
			v7 = 7*v7
			paths.append(2)
		if l3 <= 2:
			x = x*l3
			paths.append(3)
		else:
			x = 7*x
			v7 = 0-v7
			v7 = v7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))