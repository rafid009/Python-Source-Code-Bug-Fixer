import numpy as np 

def function(x):

	i7 = x
	i1 = x
	x = x
	paths = []
	try:
		if x >= 0:
			i1 = i1/6
			paths.append(1)
		else:
			i7 = i7-i7
			paths.append(2)
		if i7 < 1:
			i1 = 8*i1
			paths.append(3)
		else:
			i1 = 9-i1
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