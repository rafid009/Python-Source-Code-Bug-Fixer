import numpy as np 

def function(x):

	e4 = 1
	p7 = 5
	x = x
	paths = []
	try:
		if e4 < 2:
			e4 = e4+5
			e4 = e4/4
			e4 = e4-x
			paths.append(1)
		else:
			p7 = 6-p7
			paths.append(2)
		if e4 >= 1:
			p7 = 0/p7
			p7 = 0+e4
			p7 = p7+0
			paths.append(3)
		else:
			p7 = 3/9
			p7 = 4/x
			p7 = p7-e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))