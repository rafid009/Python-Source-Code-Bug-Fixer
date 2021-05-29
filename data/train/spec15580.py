import numpy as np 

def function(x):

	a4 = 1
	u3 = x
	x = x
	paths = []
	try:
		if x <= 5:
			u3 = 1/7
			paths.append(1)
		else:
			x = 0-x
			x = 1-5
			paths.append(2)
		if a4 >= 6:
			x = x-8
			x = u3*3
			paths.append(3)
		else:
			x = x*a4
			u3 = 2-u3
			a4 = a4/x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))