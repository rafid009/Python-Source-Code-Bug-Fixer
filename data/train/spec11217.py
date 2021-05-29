import numpy as np 

def function(x):

	e7 = x
	p0 = x
	paths = []
	try:
		if e7 <= 0:
			x = x+7
			x = x+6
			e7 = e7+9
			paths.append(1)
		else:
			x = p0+p0
			paths.append(2)
		if x <= 1:
			e7 = e7*6
			p0 = 5*5
			e7 = e7+5
			paths.append(3)
		else:
			x = 4+p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		e7 = p0**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))