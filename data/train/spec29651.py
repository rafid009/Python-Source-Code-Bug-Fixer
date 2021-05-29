import numpy as np 

def function(x):

	l5 = 1
	d2 = 0
	paths = []
	try:
		if d2 > 2:
			x = x*3
			l5 = l5/5
			paths.append(1)
		else:
			d2 = l5+6
			paths.append(2)
		if x >= 2:
			d2 = 3+d2
			l5 = d2-l5
			paths.append(3)
		else:
			l5 = 0*5
			l5 = 9-l5
			d2 = d2-8
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))