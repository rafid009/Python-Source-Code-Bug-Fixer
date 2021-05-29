import numpy as np 

def function(x):

	p3 = 7
	e1 = x
	paths = []
	try:
		if p3 >= 7:
			e1 = 1/e1
			paths.append(1)
		else:
			x = 1/4
			p3 = 6+0
			p3 = p3+p3
			paths.append(2)
		if p3 < 2:
			x = 3/x
			p3 = e1+p3
			e1 = p3-e1
			paths.append(3)
		else:
			e1 = e1/8
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))