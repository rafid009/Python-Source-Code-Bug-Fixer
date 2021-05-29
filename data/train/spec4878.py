import numpy as np 

def function(x):

	p0 = x
	e3 = x
	x = 3
	paths = []
	try:
		if e3 > 3:
			x = 4-x
			p0 = x/5
			x = p0/6
			paths.append(1)
		else:
			p0 = 5*p0
			e3 = e3*4
			paths.append(2)
		if e3 <= 0:
			x = p0-5
			e3 = 7+e3
			paths.append(3)
		else:
			e3 = x-3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))