import numpy as np 

def function(x):

	i1 = 0
	r3 = x
	paths = []
	try:
		if r3 < 3:
			i1 = i1*8
			paths.append(1)
		else:
			i1 = 3*i1
			paths.append(2)
		if r3 < 9:
			i1 = 9-2
			r3 = 2/r3
			paths.append(3)
		else:
			r3 = r3-r3
			r3 = r3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))