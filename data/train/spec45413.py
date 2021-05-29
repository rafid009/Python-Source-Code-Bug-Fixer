import numpy as np 

def function(x):

	p3 = x
	e2 = 1
	paths = []
	try:
		if p3 > 0:
			e2 = e2-2
			x = e2/x
			paths.append(1)
		else:
			x = x+7
			e2 = 5*p3
			x = x+2
			paths.append(2)
		if e2 <= 2:
			e2 = e2*1
			paths.append(3)
		else:
			x = e2+2
			p3 = p3/9
			e2 = 3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))