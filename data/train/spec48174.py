import numpy as np 

def function(x):

	o9 = 8
	b4 = 4
	paths = []
	try:
		if x <= 9:
			b4 = 5*b4
			paths.append(1)
		else:
			o9 = o9/4
			o9 = o9*9
			paths.append(2)
		if b4 > 5:
			x = x-b4
			o9 = b4+o9
			o9 = 2+o9
			paths.append(3)
		else:
			b4 = b4+8
			o9 = o9-4
			b4 = b4*o9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))