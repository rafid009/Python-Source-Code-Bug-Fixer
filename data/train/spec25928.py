import numpy as np 

def function(x):

	p3 = 2
	n1 = 5
	paths = []
	try:
		if x >= 4:
			n1 = n1-6
			p3 = x-3
			paths.append(1)
		else:
			p3 = n1-x
			n1 = n1/4
			paths.append(2)
		if n1 > 1:
			n1 = n1+2
			paths.append(3)
		else:
			n1 = n1-3
			p3 = 3-x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))