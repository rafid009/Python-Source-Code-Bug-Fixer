import numpy as np 

def function(x):

	i0 = x
	y4 = 1
	paths = []
	try:
		if y4 > 8:
			y4 = 5*y4
			paths.append(1)
		else:
			i0 = i0/4
			paths.append(2)
		if y4 > 1:
			i0 = i0-y4
			x = i0+y4
			x = x+x
			paths.append(3)
		else:
			x = x+4
			x = y4-5
			y4 = y4/5
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		y4 = i0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))