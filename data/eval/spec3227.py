import numpy as np 

def function(x):

	i1 = 6
	i4 = x
	paths = []
	try:
		if i1 > 1:
			i4 = i4/1
			i4 = 7/x
			paths.append(1)
		else:
			i1 = 6/i1
			paths.append(2)
		if i1 >= 9:
			x = x+2
			i1 = 5-i1
			paths.append(3)
		else:
			i4 = i4-3
			i4 = 7*i4
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