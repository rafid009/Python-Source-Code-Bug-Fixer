import numpy as np 

def function(x):

	o8 = 7
	b5 = 6
	paths = []
	try:
		if x < 6:
			b5 = 2+6
			paths.append(1)
		else:
			o8 = b5+o8
			paths.append(2)
		if b5 <= 2:
			b5 = b5/4
			b5 = b5*5
			paths.append(3)
		else:
			x = 7/x
			x = x-b5
			x = x+x
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