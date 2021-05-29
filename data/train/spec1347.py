import numpy as np 

def function(x):

	u5 = x
	q0 = 9
	x = x
	paths = []
	try:
		if u5 < 3:
			q0 = q0+x
			x = x/x
			u5 = 1+u5
			paths.append(1)
		else:
			q0 = x+9
			x = x/q0
			paths.append(2)
		if q0 <= 3:
			x = 1-x
			q0 = 7*q0
			paths.append(3)
		else:
			q0 = q0*7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		u5 = q0**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))