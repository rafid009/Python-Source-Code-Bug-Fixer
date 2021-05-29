import numpy as np 

def function(x):

	p0 = x
	u2 = x
	paths = []
	try:
		if x >= 7:
			p0 = u2-u2
			u2 = 3-u2
			paths.append(1)
		else:
			p0 = 4-p0
			x = 6*x
			paths.append(2)
		if x < 0:
			x = x+x
			p0 = 8+p0
			u2 = x*4
			paths.append(3)
		else:
			u2 = u2+p0
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))