import numpy as np 

def function(x):

	l5 = 7
	d0 = x
	paths = []
	try:
		if l5 < 0:
			x = x-d0
			paths.append(1)
		else:
			l5 = l5/x
			x = x*d0
			paths.append(2)
		if d0 < 8:
			d0 = d0+5
			l5 = 2*l5
			l5 = l5*7
			paths.append(3)
		else:
			x = x*8
			l5 = 2*1
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))