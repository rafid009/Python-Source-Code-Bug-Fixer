import numpy as np 

def function(x):

	d9 = 8
	l7 = x
	paths = []
	try:
		if l7 > 9:
			x = 3-3
			x = 6+l7
			paths.append(1)
		else:
			l7 = 7+l7
			d9 = d9-d9
			l7 = x+d9
			paths.append(2)
		if l7 >= 8:
			x = l7+5
			x = 3*4
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))