import numpy as np 

def function(x):

	p7 = 6
	p2 = x
	paths = []
	try:
		if p2 >= 3:
			p2 = 5*3
			paths.append(1)
		else:
			x = 4-x
			p2 = 9*p2
			p7 = p7/p7
			paths.append(2)
		if x > 4:
			p7 = p7*6
			x = 0/x
			paths.append(3)
		else:
			x = 0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))