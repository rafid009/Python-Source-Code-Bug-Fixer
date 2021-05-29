import numpy as np 

def function(x):

	l8 = 3
	d4 = 0
	paths = []
	try:
		if d4 > 4:
			x = x*0
			l8 = l8/x
			paths.append(1)
		else:
			l8 = 7*l8
			d4 = 9-d4
			paths.append(2)
		if x < 0:
			d4 = d4/5
			d4 = x*d4
			l8 = l8*3
			paths.append(3)
		else:
			l8 = l8-d4
			l8 = x/l8
			d4 = l8-1
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