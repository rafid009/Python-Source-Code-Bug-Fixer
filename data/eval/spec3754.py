import numpy as np 

def function(x):

	p8 = 0
	o9 = x
	paths = []
	try:
		if x < 6:
			o9 = x/o9
			paths.append(1)
		else:
			p8 = p8-3
			paths.append(2)
		if x < 9:
			p8 = o9+5
			paths.append(3)
		else:
			p8 = p8+o9
			p8 = 0+p8
			o9 = o9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))