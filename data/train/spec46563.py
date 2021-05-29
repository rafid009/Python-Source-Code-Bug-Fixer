import numpy as np 

def function(x):

	v6 = 4
	p0 = x
	paths = []
	try:
		if v6 <= 4:
			x = 8-x
			paths.append(1)
		else:
			x = 1*4
			paths.append(2)
		if x > 5:
			x = 6-9
			paths.append(3)
		else:
			p0 = 8-p0
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