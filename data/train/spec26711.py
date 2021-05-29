import numpy as np 

def function(x):

	d4 = 6
	p7 = 7
	paths = []
	try:
		if d4 <= 6:
			x = x+d4
			d4 = 9+d4
			d4 = d4+x
			paths.append(1)
		else:
			d4 = 5*3
			x = x+2
			paths.append(2)
		if x > 2:
			d4 = p7-d4
			paths.append(3)
		else:
			d4 = d4+7
			d4 = d4+6
			d4 = d4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))