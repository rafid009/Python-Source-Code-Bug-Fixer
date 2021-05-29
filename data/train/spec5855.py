import numpy as np 

def function(x):

	i0 = 0
	paths = []
	try:
		if x <= 4:
			x = 8+x
			x = i0+x
			i0 = i0-8
			paths.append(1)
		else:
			i0 = i0-7
			x = x/x
			x = 3*4
			paths.append(2)
		if i0 >= 6:
			x = 5*x
			i0 = x/i0
			i0 = i0-i0
			paths.append(3)
		else:
			i0 = i0-7
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