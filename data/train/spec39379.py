import numpy as np 

def function(x):

	u3 = 4
	x0 = 3
	x = x
	paths = []
	try:
		if u3 <= 3:
			u3 = 7-u3
			x0 = 6-4
			x = x+6
			paths.append(1)
		else:
			x = x/6
			u3 = u3-x
			x0 = x0*5
			paths.append(2)
		if x < 6:
			u3 = 5*u3
			paths.append(3)
		else:
			x = 3+x
			u3 = 6-x0
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x0 = u3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))