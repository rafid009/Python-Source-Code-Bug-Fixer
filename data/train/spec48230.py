import numpy as np 

def function(x):

	i4 = x
	x2 = x
	paths = []
	try:
		if x >= 5:
			x2 = x2/i4
			paths.append(1)
		else:
			i4 = 2-i4
			paths.append(2)
		if x2 >= 6:
			x = i4*7
			i4 = x2/i4
			x2 = x2/5
			paths.append(3)
		else:
			x = x2*2
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))