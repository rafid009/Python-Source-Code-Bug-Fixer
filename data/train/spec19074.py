import numpy as np 

def function(x):

	o4 = 8
	b2 = 7
	paths = []
	try:
		if b2 > 0:
			o4 = o4/o4
			x = 1-4
			b2 = 5/2
			paths.append(1)
		else:
			b2 = 9*9
			paths.append(2)
		if o4 >= 8:
			x = x-x
			b2 = 7*b2
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))