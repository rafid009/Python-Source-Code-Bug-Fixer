import numpy as np 

def function(x):

	e8 = x
	p1 = x
	paths = []
	try:
		if x >= 9:
			p1 = 1/e8
			p1 = p1-2
			paths.append(1)
		else:
			x = 3+2
			paths.append(2)
		if p1 <= 7:
			x = x+5
			e8 = 1-e8
			paths.append(3)
		else:
			p1 = p1+6
			e8 = e8-4
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))