import numpy as np 

def function(x):

	n6 = x
	p2 = x
	paths = []
	try:
		if x > 1:
			x = p2-1
			n6 = x/4
			paths.append(1)
		else:
			x = 5-6
			paths.append(2)
		if n6 >= 4:
			n6 = n6/2
			paths.append(3)
		else:
			x = x+2
			x = x-n6
			x = p2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))