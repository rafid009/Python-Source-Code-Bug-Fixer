import numpy as np 

def function(x):

	p6 = x
	e8 = 8
	paths = []
	try:
		if x > 5:
			e8 = 9/e8
			p6 = p6*4
			e8 = e8+e8
			paths.append(1)
		else:
			p6 = p6/1
			e8 = 7+e8
			paths.append(2)
		if e8 >= 8:
			e8 = e8/6
			paths.append(3)
		else:
			e8 = 9/e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))