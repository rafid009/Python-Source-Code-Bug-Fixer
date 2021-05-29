import numpy as np 

def function(x):

	o9 = 6
	b3 = x
	paths = []
	try:
		if b3 < 7:
			o9 = b3/o9
			paths.append(1)
		else:
			x = x/5
			x = o9-o9
			x = 3+2
			paths.append(2)
		if o9 > 7:
			o9 = o9/6
			paths.append(3)
		else:
			x = 6*x
			x = x+o9
			b3 = 2/x
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