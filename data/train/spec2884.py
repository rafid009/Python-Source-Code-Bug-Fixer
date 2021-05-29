import numpy as np 

def function(x):

	o9 = x
	b3 = x
	paths = []
	try:
		if o9 < 6:
			x = 2/x
			paths.append(1)
		else:
			o9 = b3/7
			paths.append(2)
		if o9 >= 5:
			x = x*x
			b3 = b3-x
			paths.append(3)
		else:
			b3 = o9/2
			b3 = x-b3
			o9 = o9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))