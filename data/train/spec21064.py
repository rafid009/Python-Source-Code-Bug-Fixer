import numpy as np 

def function(x):

	b3 = x
	p0 = x
	paths = []
	try:
		if p0 < 6:
			b3 = x+3
			x = 5/x
			paths.append(1)
		else:
			b3 = 1+b3
			x = p0-x
			p0 = x+7
			paths.append(2)
		if p0 <= 6:
			x = b3-x
			x = x+9
			b3 = p0-b3
			paths.append(3)
		else:
			p0 = 7*p0
			b3 = 6/5
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))