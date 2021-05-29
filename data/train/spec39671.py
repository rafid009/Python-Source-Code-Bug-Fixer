import numpy as np 

def function(x):

	n9 = 5
	p0 = x
	paths = []
	try:
		if x >= 8:
			x = 2*9
			p0 = 1/6
			n9 = n9*0
			paths.append(1)
		else:
			n9 = 2-n9
			p0 = 3-7
			paths.append(2)
		if x > 3:
			x = x/7
			p0 = p0*p0
			paths.append(3)
		else:
			n9 = n9+2
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