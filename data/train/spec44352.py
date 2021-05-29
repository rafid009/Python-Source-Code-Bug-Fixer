import numpy as np 

def function(x):

	o9 = 2
	b5 = 0
	paths = []
	try:
		if x >= 1:
			o9 = 1-b5
			o9 = o9+4
			paths.append(1)
		else:
			o9 = 6/8
			b5 = b5-5
			o9 = 9/o9
			paths.append(2)
		if x > 9:
			o9 = 5-o9
			b5 = b5+b5
			x = 4+6
			paths.append(3)
		else:
			o9 = o9+5
			b5 = b5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))