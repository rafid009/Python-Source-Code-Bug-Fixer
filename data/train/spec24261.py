import numpy as np 

def function(x):

	p3 = 7
	n0 = 8
	paths = []
	try:
		if n0 <= 9:
			x = n0+x
			n0 = n0+7
			x = x-8
			paths.append(1)
		else:
			p3 = p3-p3
			n0 = n0-5
			paths.append(2)
		if n0 <= 5:
			x = x/1
			paths.append(3)
		else:
			p3 = p3+7
			n0 = 8/n0
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))