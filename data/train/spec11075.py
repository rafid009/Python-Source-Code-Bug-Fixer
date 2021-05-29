import numpy as np 

def function(x):

	p0 = x
	f3 = x
	paths = []
	try:
		if x < 4:
			p0 = p0+f3
			paths.append(1)
		else:
			x = 9-x
			f3 = 2/f3
			paths.append(2)
		if f3 < 4:
			f3 = 1/f3
			x = x*7
			paths.append(3)
		else:
			f3 = p0/6
			f3 = 2-f3
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