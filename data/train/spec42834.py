import numpy as np 

def function(x):

	e2 = 1
	q5 = x
	paths = []
	try:
		if e2 > 8:
			x = q5*4
			paths.append(1)
		else:
			q5 = 2-9
			paths.append(2)
		if x <= 0:
			x = x/5
			e2 = e2*6
			paths.append(3)
		else:
			e2 = e2*8
			q5 = q5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))