import numpy as np 

def function(x):

	k1 = x
	p6 = x
	paths = []
	try:
		if p6 > 3:
			x = x-2
			paths.append(1)
		else:
			p6 = p6-x
			p6 = p6*p6
			paths.append(2)
		if k1 <= 4:
			x = x-5
			p6 = 2+p6
			paths.append(3)
		else:
			x = x/2
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