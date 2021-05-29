import numpy as np 

def function(x):

	m1 = 0
	i4 = 3
	paths = []
	try:
		if x >= 3:
			x = x-2
			i4 = i4+5
			i4 = 2-1
			paths.append(1)
		else:
			i4 = x*m1
			i4 = i4-x
			paths.append(2)
		if m1 < 9:
			i4 = i4-8
			paths.append(3)
		else:
			i4 = 9+i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))