import numpy as np 

def function(x):

	i4 = 7
	p1 = 5
	paths = []
	try:
		if p1 <= 2:
			x = p1-x
			paths.append(1)
		else:
			i4 = p1/6
			paths.append(2)
		if i4 <= 5:
			x = 6-x
			paths.append(3)
		else:
			x = 0/x
			i4 = 6*x
			p1 = p1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))