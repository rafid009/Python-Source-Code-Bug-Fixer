import numpy as np 

def function(x):

	i8 = 8
	p4 = 6
	paths = []
	try:
		if p4 < 5:
			x = x/p4
			paths.append(1)
		else:
			i8 = i8-5
			i8 = i8+x
			paths.append(2)
		if x < 6:
			i8 = i8-9
			x = x*7
			i8 = i8*x
			paths.append(3)
		else:
			x = x*4
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