import numpy as np 

def function(x):

	p1 = 1
	d4 = x
	paths = []
	try:
		if x <= 6:
			x = x/x
			paths.append(1)
		else:
			x = p1-x
			paths.append(2)
		if p1 >= 3:
			d4 = 3-7
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))