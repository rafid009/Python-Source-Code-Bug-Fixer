import numpy as np 

def function(x):

	p0 = 6
	a5 = x
	paths = []
	try:
		if x < 7:
			a5 = a5-9
			p0 = 2/x
			a5 = 8*x
			paths.append(1)
		else:
			a5 = a5/a5
			paths.append(2)
		if x < 9:
			a5 = 1-a5
			paths.append(3)
		else:
			a5 = 6+a5
			p0 = p0-4
			p0 = 6*p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		a5 = p0**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))