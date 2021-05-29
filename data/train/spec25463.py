import numpy as np 

def function(x):

	v3 = 4
	u0 = x
	paths = []
	try:
		if v3 <= 5:
			v3 = v3+v3
			v3 = 5*7
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x <= 2:
			u0 = 5-v3
			u0 = u0-x
			x = v3-7
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))