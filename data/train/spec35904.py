import numpy as np 

def function(x):

	e4 = 8
	b0 = 9
	paths = []
	try:
		if x > 3:
			x = x*0
			paths.append(1)
		else:
			b0 = 0+e4
			e4 = e4+4
			paths.append(2)
		if b0 >= 7:
			e4 = 9-e4
			b0 = 1+b0
			paths.append(3)
		else:
			b0 = b0*4
			e4 = e4+b0
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