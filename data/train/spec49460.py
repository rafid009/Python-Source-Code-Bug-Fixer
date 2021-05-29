import numpy as np 

def function(x):

	b9 = 9
	o1 = 7
	paths = []
	try:
		if o1 <= 8:
			o1 = 7/o1
			x = 9/x
			paths.append(1)
		else:
			o1 = o1-b9
			o1 = 4/o1
			x = x*4
			paths.append(2)
		if o1 > 0:
			b9 = b9/6
			b9 = 8*7
			paths.append(3)
		else:
			b9 = 0/x
			b9 = o1/b9
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