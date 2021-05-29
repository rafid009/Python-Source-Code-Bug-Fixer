import numpy as np 

def function(x):

	q1 = x
	a1 = x
	x = x
	paths = []
	try:
		if q1 > 6:
			a1 = a1+q1
			q1 = q1-6
			q1 = x*3
			paths.append(1)
		else:
			a1 = a1+5
			paths.append(2)
		if q1 > 9:
			q1 = 6/3
			q1 = q1+3
			paths.append(3)
		else:
			x = a1+x
			x = a1+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))