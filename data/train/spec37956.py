import numpy as np 

def function(x):

	b6 = 0
	o4 = 7
	paths = []
	try:
		if b6 > 0:
			x = x*x
			b6 = 3/b6
			o4 = 4-4
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if o4 > 1:
			o4 = o4-x
			x = x-4
			paths.append(3)
		else:
			x = 2+o4
			b6 = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))