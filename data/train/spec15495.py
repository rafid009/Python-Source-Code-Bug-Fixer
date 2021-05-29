import numpy as np 

def function(x):

	r1 = x
	v7 = x
	paths = []
	try:
		if x < 0:
			x = 2/x
			paths.append(1)
		else:
			x = 6+1
			paths.append(2)
		if r1 >= 8:
			x = x-9
			paths.append(3)
		else:
			v7 = v7-9
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))