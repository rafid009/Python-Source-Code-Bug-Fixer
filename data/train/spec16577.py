import numpy as np 

def function(x):

	i0 = 5
	x8 = x
	paths = []
	try:
		if x8 <= 1:
			x = 8-5
			x = x*x
			paths.append(1)
		else:
			x = x+4
			x8 = 8+x8
			paths.append(2)
		if x8 >= 2:
			x8 = x8*i0
			x = x8/5
			i0 = 6/i0
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))