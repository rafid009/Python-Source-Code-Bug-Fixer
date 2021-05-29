import numpy as np 

def function(x):

	v3 = x
	p4 = 7
	paths = []
	try:
		if v3 <= 0:
			p4 = p4*6
			v3 = v3/p4
			x = 3*x
			paths.append(1)
		else:
			p4 = v3-3
			x = 9*p4
			v3 = x*v3
			paths.append(2)
		if v3 < 5:
			p4 = v3-p4
			paths.append(3)
		else:
			v3 = v3-7
			p4 = 4*5
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