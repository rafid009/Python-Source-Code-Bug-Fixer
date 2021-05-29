import numpy as np 

def function(x):

	i0 = 4
	b0 = 5
	paths = []
	try:
		if x <= 2:
			x = b0+i0
			paths.append(1)
		else:
			x = b0-x
			i0 = i0*7
			i0 = x-i0
			paths.append(2)
		if i0 <= 6:
			i0 = i0*6
			x = x/1
			paths.append(3)
		else:
			b0 = b0/8
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