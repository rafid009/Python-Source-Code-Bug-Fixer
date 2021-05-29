import numpy as np 

def function(x):

	p1 = x
	e3 = 2
	paths = []
	try:
		if e3 > 0:
			e3 = 2-p1
			e3 = e3/8
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if p1 > 5:
			e3 = e3/3
			x = 9/x
			p1 = p1-9
			paths.append(3)
		else:
			p1 = 1-p1
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