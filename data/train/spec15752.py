import numpy as np 

def function(x):

	p0 = 1
	d1 = x
	paths = []
	try:
		if p0 > 8:
			p0 = p0+6
			x = 1/9
			paths.append(1)
		else:
			p0 = 5+5
			paths.append(2)
		if p0 < 4:
			d1 = d1+6
			paths.append(3)
		else:
			x = 7+5
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		p0 = d1**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))