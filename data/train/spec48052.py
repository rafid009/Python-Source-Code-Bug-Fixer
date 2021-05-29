import numpy as np 

def function(x):

	d6 = 4
	s8 = 8
	paths = []
	try:
		if d6 < 4:
			x = s8*5
			s8 = x+x
			paths.append(1)
		else:
			x = s8*x
			paths.append(2)
		if d6 > 9:
			d6 = d6-9
			paths.append(3)
		else:
			d6 = d6+8
			d6 = s8*d6
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