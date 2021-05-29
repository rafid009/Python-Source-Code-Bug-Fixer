import numpy as np 

def function(x):

	u1 = 1
	e5 = 5
	paths = []
	try:
		if x >= 0:
			x = 9*x
			e5 = u1*x
			paths.append(1)
		else:
			e5 = 2-e5
			x = 0*x
			paths.append(2)
		if e5 <= 3:
			x = e5*1
			paths.append(3)
		else:
			u1 = 0-1
			e5 = 6-e5
			u1 = 1+7
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))