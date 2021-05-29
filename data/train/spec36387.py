import numpy as np 

def function(x):

	o1 = 7
	b8 = 1
	paths = []
	try:
		if o1 >= 6:
			b8 = b8*b8
			paths.append(1)
		else:
			o1 = 7/5
			paths.append(2)
		if b8 <= 6:
			b8 = 0+8
			o1 = 6+o1
			paths.append(3)
		else:
			b8 = b8/6
			x = x-o1
			o1 = o1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))