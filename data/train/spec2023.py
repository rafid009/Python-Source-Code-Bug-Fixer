import numpy as np 

def function(x):

	p1 = 1
	d4 = 6
	paths = []
	try:
		if x < 4:
			d4 = d4+x
			paths.append(1)
		else:
			p1 = p1/x
			paths.append(2)
		if p1 < 9:
			x = x+4
			p1 = x/1
			paths.append(3)
		else:
			p1 = x/d4
			p1 = p1/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))