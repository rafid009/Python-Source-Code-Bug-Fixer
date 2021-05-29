import numpy as np 

def function(x):

	p1 = 7
	e1 = x
	paths = []
	try:
		if p1 < 8:
			x = x/7
			paths.append(1)
		else:
			e1 = 6+3
			p1 = p1/x
			p1 = 3/x
			paths.append(2)
		if p1 >= 2:
			p1 = e1+p1
			e1 = e1+6
			x = x-9
			paths.append(3)
		else:
			e1 = e1/e1
			e1 = e1*x
			e1 = e1*4
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		e1 = p1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))