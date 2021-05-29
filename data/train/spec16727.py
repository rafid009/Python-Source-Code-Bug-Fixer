import numpy as np 

def function(x):

	p0 = x
	u2 = 2
	paths = []
	try:
		if u2 >= 6:
			x = x-0
			x = 2+2
			paths.append(1)
		else:
			x = x/u2
			paths.append(2)
		if u2 >= 4:
			p0 = x*p0
			x = 6*x
			u2 = u2+0
			paths.append(3)
		else:
			x = x/9
			x = p0/x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))