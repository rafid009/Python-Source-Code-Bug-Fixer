import numpy as np 

def function(x):

	q1 = x
	e0 = 9
	paths = []
	try:
		if q1 <= 8:
			x = x-8
			e0 = 1/x
			q1 = q1+x
			paths.append(1)
		else:
			e0 = x*4
			paths.append(2)
		if e0 > 8:
			e0 = e0+3
			paths.append(3)
		else:
			x = e0/q1
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))