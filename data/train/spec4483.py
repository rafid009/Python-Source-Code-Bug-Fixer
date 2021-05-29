import numpy as np 

def function(x):

	p6 = x
	e7 = x
	paths = []
	try:
		if p6 > 5:
			p6 = e7*p6
			paths.append(1)
		else:
			e7 = 5/p6
			p6 = p6*e7
			paths.append(2)
		if e7 > 8:
			e7 = e7+x
			x = 9-x
			paths.append(3)
		else:
			x = 2-0
			p6 = p6+x
			p6 = e7*p6
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))