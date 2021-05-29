import numpy as np 

def function(x):

	p3 = 6
	f3 = x
	paths = []
	try:
		if x >= 0:
			x = x*9
			p3 = 0/x
			x = 2*x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if p3 < 7:
			f3 = 2*f3
			x = 2-x
			x = f3+x
			paths.append(3)
		else:
			f3 = f3*f3
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