import numpy as np 

def function(x):

	p0 = x
	n4 = x
	x = 1
	paths = []
	try:
		if p0 <= 3:
			x = 0+p0
			n4 = n4/7
			paths.append(1)
		else:
			p0 = p0+2
			p0 = p0+3
			p0 = x+p0
			paths.append(2)
		if n4 <= 3:
			x = 7/x
			x = x*3
			n4 = n4+6
			paths.append(3)
		else:
			x = 4/6
			n4 = n4*7
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		p0 = n4**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))