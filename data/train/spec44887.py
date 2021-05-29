import numpy as np 

def function(x):

	p3 = 4
	n3 = x
	paths = []
	try:
		if p3 < 6:
			p3 = n3/4
			paths.append(1)
		else:
			x = x-9
			p3 = 4-x
			paths.append(2)
		if p3 > 6:
			x = n3/5
			n3 = 3/n3
			paths.append(3)
		else:
			p3 = x-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))