import numpy as np 

def function(x):

	i0 = 5
	n1 = x
	paths = []
	try:
		if x > 2:
			x = 2/x
			x = 0*x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if n1 < 5:
			i0 = i0-x
			i0 = 5-x
			paths.append(3)
		else:
			i0 = i0*5
			x = 7+x
			x = i0/5
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