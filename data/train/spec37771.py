import numpy as np 

def function(x):

	e6 = 5
	q7 = 4
	paths = []
	try:
		if e6 < 0:
			x = x*4
			e6 = e6*6
			paths.append(1)
		else:
			e6 = e6/3
			e6 = e6-9
			x = x/4
			paths.append(2)
		if x < 0:
			q7 = 9+x
			paths.append(3)
		else:
			q7 = x/q7
			x = 7*x
			e6 = 6-x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))