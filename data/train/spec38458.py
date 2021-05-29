import numpy as np 

def function(x):

	i8 = x
	p0 = 3
	paths = []
	try:
		if i8 >= 4:
			x = x-9
			i8 = i8+5
			paths.append(1)
		else:
			i8 = i8/7
			paths.append(2)
		if x <= 2:
			x = i8+4
			p0 = p0*4
			p0 = 4+8
			paths.append(3)
		else:
			i8 = 0/i8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))