import numpy as np 

def function(x):

	i0 = x
	h2 = x
	paths = []
	try:
		if h2 < 0:
			i0 = h2-x
			x = x*6
			paths.append(1)
		else:
			i0 = 7-x
			i0 = 7+x
			paths.append(2)
		if h2 >= 5:
			i0 = i0*3
			i0 = 7-i0
			paths.append(3)
		else:
			i0 = 0+4
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		i0 = h2**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))