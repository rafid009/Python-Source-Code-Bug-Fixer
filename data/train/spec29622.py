import numpy as np 

def function(x):

	e4 = x
	d2 = 1
	paths = []
	try:
		if d2 > 3:
			x = 7+d2
			x = 1-x
			paths.append(1)
		else:
			x = 8-x
			e4 = d2/2
			e4 = x/e4
			paths.append(2)
		if d2 <= 2:
			d2 = 4+8
			d2 = x+2
			paths.append(3)
		else:
			x = x*7
			d2 = d2+x
			d2 = d2/1
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		d2 = e4**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))