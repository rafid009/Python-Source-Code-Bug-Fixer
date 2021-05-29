import numpy as np 

def function(x):

	a4 = 6
	u3 = 4
	paths = []
	try:
		if x < 2:
			a4 = 4-4
			paths.append(1)
		else:
			x = 0-x
			u3 = a4-u3
			u3 = x+u3
			paths.append(2)
		if u3 >= 1:
			u3 = u3-u3
			a4 = 3-5
			paths.append(3)
		else:
			a4 = 9-a4
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))