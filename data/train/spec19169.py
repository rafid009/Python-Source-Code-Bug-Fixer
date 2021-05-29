import numpy as np 

def function(x):

	d0 = 8
	p4 = x
	paths = []
	try:
		if d0 > 8:
			d0 = d0+0
			x = 6/x
			d0 = 3*5
			paths.append(1)
		else:
			d0 = 1-p4
			x = x+d0
			d0 = 9/d0
			paths.append(2)
		if p4 < 8:
			p4 = x/9
			paths.append(3)
		else:
			p4 = 2-9
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))