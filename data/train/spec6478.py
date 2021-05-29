import numpy as np 

def function(x):

	p8 = 7
	o2 = 5
	paths = []
	try:
		if o2 < 6:
			o2 = 8*7
			x = 8*x
			paths.append(1)
		else:
			o2 = 1+7
			p8 = p8*5
			o2 = 8+o2
			paths.append(2)
		if x > 7:
			o2 = 0*o2
			o2 = 2-o2
			o2 = 1*o2
			paths.append(3)
		else:
			p8 = p8-3
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