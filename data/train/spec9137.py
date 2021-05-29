import numpy as np 

def function(x):

	q1 = x
	e2 = 6
	paths = []
	try:
		if e2 < 4:
			x = x*e2
			q1 = q1*x
			e2 = 2-2
			paths.append(1)
		else:
			e2 = e2+q1
			x = x*x
			paths.append(2)
		if q1 >= 4:
			e2 = 0/4
			q1 = q1+6
			paths.append(3)
		else:
			e2 = e2-5
			e2 = 2*e2
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))