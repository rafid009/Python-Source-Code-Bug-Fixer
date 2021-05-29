import numpy as np 

def function(x):

	e3 = x
	q1 = x
	paths = []
	try:
		if q1 <= 5:
			q1 = 8/9
			paths.append(1)
		else:
			x = 5+x
			x = 6/9
			paths.append(2)
		if q1 > 9:
			x = x/4
			q1 = 9*7
			paths.append(3)
		else:
			e3 = e3+x
			x = x+6
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		q1 = e3**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))