import numpy as np 

def function(x):

	e5 = x
	f0 = 6
	paths = []
	try:
		if e5 < 2:
			e5 = x*1
			paths.append(1)
		else:
			f0 = f0*x
			e5 = 2/4
			x = f0-7
			paths.append(2)
		if x > 8:
			x = 1/x
			f0 = 1/8
			f0 = f0-6
			paths.append(3)
		else:
			f0 = 0+e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))