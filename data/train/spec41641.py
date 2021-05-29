import numpy as np 

def function(x):

	d4 = x
	l4 = x
	paths = []
	try:
		if l4 >= 9:
			l4 = 4-l4
			x = x+3
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if l4 <= 0:
			x = 5-x
			x = x*6
			d4 = 0*x
			paths.append(3)
		else:
			d4 = d4+0
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