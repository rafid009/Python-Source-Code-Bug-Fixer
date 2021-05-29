import numpy as np 

def function(x):

	l9 = 7
	d8 = 8
	paths = []
	try:
		if d8 < 1:
			l9 = l9/1
			d8 = 7*d8
			l9 = d8+l9
			paths.append(1)
		else:
			d8 = l9-l9
			paths.append(2)
		if l9 >= 9:
			x = l9-x
			x = x*1
			d8 = d8+3
			paths.append(3)
		else:
			l9 = 0-x
			d8 = d8+6
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