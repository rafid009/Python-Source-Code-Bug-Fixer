import numpy as np 

def function(x):

	p8 = x
	p4 = 0
	paths = []
	try:
		if p8 > 3:
			p8 = p8-2
			p4 = x*1
			p8 = p8-x
			paths.append(1)
		else:
			x = x/p8
			x = p8-1
			p4 = 3-p4
			paths.append(2)
		if x >= 3:
			p4 = p4*x
			p8 = p8/1
			x = x-6
			paths.append(3)
		else:
			x = 6+x
			x = 8/x
			p8 = p8/x
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