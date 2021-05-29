import numpy as np 

def function(x):

	e2 = x
	u6 = x
	paths = []
	try:
		if x <= 2:
			e2 = 7/e2
			paths.append(1)
		else:
			x = x*8
			x = 0*e2
			paths.append(2)
		if x < 5:
			e2 = e2/e2
			paths.append(3)
		else:
			e2 = e2/9
			x = x+e2
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		e2 = u6**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))