import numpy as np 

def function(x):

	p7 = 9
	a2 = x
	paths = []
	try:
		if a2 >= 9:
			p7 = p7+p7
			a2 = x+a2
			x = x-x
			paths.append(1)
		else:
			p7 = 8-p7
			a2 = 9-x
			paths.append(2)
		if x < 3:
			p7 = 4/4
			p7 = 2+5
			paths.append(3)
		else:
			x = 3-x
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