import numpy as np 

def function(x):

	u1 = x
	q0 = x
	paths = []
	try:
		if u1 > 9:
			q0 = u1*3
			paths.append(1)
		else:
			q0 = q0-3
			paths.append(2)
		if x <= 9:
			x = x*9
			x = x-7
			paths.append(3)
		else:
			u1 = u1+x
			u1 = 1*q0
			u1 = 8-u1
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		u1 = q0**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))