import numpy as np 

def function(x):

	p0 = x
	x2 = x
	paths = []
	try:
		if x2 <= 7:
			x2 = x2*1
			paths.append(1)
		else:
			x2 = x2-9
			p0 = 1+p0
			x = x2*x2
			paths.append(2)
		if p0 >= 2:
			x2 = x2/6
			x2 = p0/7
			paths.append(3)
		else:
			x = x-0
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