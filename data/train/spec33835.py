import numpy as np 

def function(x):

	e3 = x
	q0 = 3
	paths = []
	try:
		if q0 > 6:
			x = x+5
			x = x*7
			paths.append(1)
		else:
			x = 0-4
			x = 9-x
			paths.append(2)
		if x < 6:
			e3 = e3-0
			q0 = 6-8
			e3 = 3+e3
			paths.append(3)
		else:
			x = 8+x
			q0 = x/9
			e3 = 1-q0
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		q0 = e3**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))