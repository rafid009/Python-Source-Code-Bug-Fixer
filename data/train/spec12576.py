import numpy as np 

def function(x):

	i1 = 5
	i8 = x
	paths = []
	try:
		if i1 > 0:
			x = 7*x
			paths.append(1)
		else:
			x = x-i1
			i1 = i1+i1
			paths.append(2)
		if i1 < 4:
			i8 = 8/7
			paths.append(3)
		else:
			i8 = i8/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))