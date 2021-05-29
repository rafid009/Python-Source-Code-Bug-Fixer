import numpy as np 

def function(x):

	i0 = x
	u2 = 8
	paths = []
	try:
		if i0 >= 1:
			i0 = 2/i0
			u2 = u2*x
			i0 = 3/i0
			paths.append(1)
		else:
			i0 = i0+i0
			i0 = 8+i0
			u2 = i0+u2
			paths.append(2)
		if i0 > 5:
			i0 = u2/i0
			u2 = 4+3
			u2 = 3+x
			paths.append(3)
		else:
			u2 = u2/u2
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))