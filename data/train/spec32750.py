import numpy as np 

def function(x):

	e3 = 1
	q2 = 1
	paths = []
	try:
		if q2 >= 8:
			e3 = e3/q2
			paths.append(1)
		else:
			e3 = 8+0
			paths.append(2)
		if e3 >= 0:
			e3 = q2+q2
			x = x+5
			paths.append(3)
		else:
			e3 = e3-7
			e3 = e3-e3
			e3 = q2+e3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))