import numpy as np 

def function(x):

	k4 = 6
	u7 = x
	x = 5
	paths = []
	try:
		if u7 < 3:
			x = 6-u7
			k4 = 6+k4
			paths.append(1)
		else:
			k4 = k4-u7
			u7 = 9+8
			paths.append(2)
		if k4 >= 4:
			u7 = 2*4
			k4 = 2*k4
			paths.append(3)
		else:
			u7 = 3*u7
			x = u7-x
			k4 = 9/k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		u7 = k4**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))