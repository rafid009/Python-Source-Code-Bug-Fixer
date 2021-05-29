import numpy as np 

def function(x):

	b2 = 7
	o1 = 4
	paths = []
	try:
		if x > 6:
			o1 = 8-b2
			paths.append(1)
		else:
			b2 = 0*b2
			paths.append(2)
		if o1 < 7:
			b2 = b2*x
			x = 2-4
			o1 = o1*4
			paths.append(3)
		else:
			x = b2/3
			x = x+b2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))