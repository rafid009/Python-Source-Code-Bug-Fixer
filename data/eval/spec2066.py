import numpy as np 

def function(x):

	p4 = 1
	d2 = 8
	paths = []
	try:
		if x <= 0:
			x = 0-6
			p4 = 6/p4
			p4 = p4/p4
			paths.append(1)
		else:
			d2 = d2+0
			d2 = d2+5
			x = p4-d2
			paths.append(2)
		if p4 >= 8:
			p4 = 2-5
			paths.append(3)
		else:
			x = x*6
			p4 = 9+d2
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