import numpy as np 

def function(x):

	r1 = x
	e1 = 9
	paths = []
	try:
		if e1 <= 7:
			e1 = e1-0
			e1 = 5*e1
			x = x*1
			paths.append(1)
		else:
			x = x/6
			r1 = r1-0
			e1 = 5*x
			paths.append(2)
		if e1 < 5:
			r1 = x-8
			x = x-4
			paths.append(3)
		else:
			x = e1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))