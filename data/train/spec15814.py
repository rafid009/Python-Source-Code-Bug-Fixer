import numpy as np 

def function(x):

	u3 = x
	a3 = x
	paths = []
	try:
		if a3 <= 6:
			x = 3/x
			paths.append(1)
		else:
			a3 = a3*3
			a3 = 3+u3
			paths.append(2)
		if x >= 2:
			x = u3+7
			paths.append(3)
		else:
			x = 5/x
			x = x-x
			u3 = 1+u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))