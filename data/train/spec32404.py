import numpy as np 

def function(x):

	u4 = 0
	p4 = 6
	paths = []
	try:
		if x >= 2:
			p4 = 5+p4
			u4 = 3*u4
			x = 4*x
			paths.append(1)
		else:
			x = x/6
			u4 = 0+u4
			paths.append(2)
		if p4 < 6:
			p4 = 7-3
			p4 = 8+4
			paths.append(3)
		else:
			u4 = 2*2
			u4 = u4/u4
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