import numpy as np 

def function(x):

	u5 = 5
	q2 = x
	paths = []
	try:
		if q2 > 5:
			x = x/4
			x = q2*x
			u5 = 4+u5
			paths.append(1)
		else:
			u5 = 3/u5
			paths.append(2)
		if q2 <= 4:
			q2 = 9-9
			u5 = x+u5
			paths.append(3)
		else:
			q2 = 1-9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))