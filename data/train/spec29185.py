import numpy as np 

def function(x):

	u9 = x
	q0 = x
	paths = []
	try:
		if u9 >= 4:
			u9 = q0/3
			q0 = 4*q0
			paths.append(1)
		else:
			q0 = u9+0
			paths.append(2)
		if u9 <= 5:
			u9 = u9/8
			x = 8*x
			u9 = u9+2
			paths.append(3)
		else:
			u9 = u9*4
			q0 = q0-3
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))