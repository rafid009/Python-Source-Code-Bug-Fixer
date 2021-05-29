import numpy as np 

def function(x):

	d1 = x
	p4 = 6
	paths = []
	try:
		if d1 >= 7:
			x = x/4
			d1 = 7*8
			p4 = 3*6
			paths.append(1)
		else:
			p4 = p4/4
			p4 = p4*6
			paths.append(2)
		if x < 7:
			p4 = x*4
			paths.append(3)
		else:
			p4 = p4-p4
			x = x*d1
			x = x*d1
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