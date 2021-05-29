import numpy as np 

def function(x):

	o9 = 4
	p3 = x
	paths = []
	try:
		if x <= 3:
			p3 = 3/x
			p3 = 6-4
			paths.append(1)
		else:
			p3 = 6/p3
			p3 = p3/5
			p3 = 8*o9
			paths.append(2)
		if p3 >= 3:
			o9 = o9+o9
			x = p3*5
			o9 = 7+o9
			paths.append(3)
		else:
			x = 8*x
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