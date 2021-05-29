import numpy as np 

def function(x):

	x9 = 8
	u3 = 6
	x = 2
	paths = []
	try:
		if x <= 9:
			x = x/5
			u3 = 8-6
			x9 = x*u3
			paths.append(1)
		else:
			x = 8+x
			x9 = x9-x
			x9 = x9+1
			paths.append(2)
		if x < 0:
			u3 = u3+x
			paths.append(3)
		else:
			x = x-x9
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