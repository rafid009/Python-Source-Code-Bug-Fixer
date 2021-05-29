import numpy as np 

def function(x):

	i1 = 0
	x4 = x
	paths = []
	try:
		if i1 <= 9:
			i1 = i1-5
			paths.append(1)
		else:
			x4 = 8+x4
			x4 = 2*x
			paths.append(2)
		if i1 > 0:
			x = 3-i1
			paths.append(3)
		else:
			i1 = i1-2
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))