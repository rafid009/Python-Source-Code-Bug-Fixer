import numpy as np 

def function(x):

	e5 = x
	u3 = 6
	paths = []
	try:
		if e5 < 0:
			u3 = 7/e5
			e5 = x*e5
			u3 = u3+6
			paths.append(1)
		else:
			u3 = 7-u3
			paths.append(2)
		if x >= 0:
			u3 = u3*3
			e5 = e5-e5
			paths.append(3)
		else:
			e5 = 2-4
			u3 = x+e5
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		e5 = u3**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))