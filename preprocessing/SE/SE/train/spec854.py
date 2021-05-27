import numpy as np 

def function(x):

	l8 = 2
	d5 = x
	paths = []
	try:
		if l8 < 5:
			x = d5*x
			paths.append(1)
		else:
			l8 = x/l8
			paths.append(2)
		if x < 4:
			l8 = l8*6
			x = x*x
			paths.append(3)
		else:
			d5 = 5+x
			d5 = d5/2
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))