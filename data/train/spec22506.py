import numpy as np 

def function(x):

	l8 = 5
	d6 = x
	paths = []
	try:
		if l8 <= 2:
			d6 = 4-l8
			x = 8+x
			paths.append(1)
		else:
			x = 7-x
			x = x-x
			paths.append(2)
		if l8 > 4:
			x = 8*x
			l8 = l8*8
			paths.append(3)
		else:
			l8 = 5-l8
			l8 = l8+5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))