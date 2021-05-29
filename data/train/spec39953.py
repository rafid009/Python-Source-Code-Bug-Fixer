import numpy as np 

def function(x):

	p7 = x
	u0 = 8
	paths = []
	try:
		if x <= 1:
			u0 = x/8
			paths.append(1)
		else:
			x = x-u0
			p7 = p7+p7
			x = x*8
			paths.append(2)
		if u0 <= 5:
			x = u0-x
			paths.append(3)
		else:
			u0 = u0*u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))