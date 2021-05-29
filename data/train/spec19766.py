import numpy as np 

def function(x):

	r6 = x
	i0 = 2
	paths = []
	try:
		if x > 1:
			i0 = 0-x
			r6 = 5/7
			paths.append(1)
		else:
			x = x+x
			x = 2*x
			i0 = i0+8
			paths.append(2)
		if x < 1:
			x = 5/x
			r6 = x/r6
			i0 = i0+3
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))