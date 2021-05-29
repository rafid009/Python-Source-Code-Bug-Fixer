import numpy as np 

def function(x):

	q0 = x
	u9 = x
	paths = []
	try:
		if x >= 8:
			u9 = 4*1
			x = q0*3
			q0 = 3*x
			paths.append(1)
		else:
			u9 = x-u9
			x = 9-x
			x = u9/x
			paths.append(2)
		if q0 > 7:
			x = x-q0
			q0 = q0-1
			u9 = q0/x
			paths.append(3)
		else:
			x = q0-8
			q0 = u9+q0
			q0 = x-u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))