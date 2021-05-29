import numpy as np 

def function(x):

	u2 = 7
	q6 = x
	paths = []
	try:
		if q6 >= 3:
			u2 = 4-1
			paths.append(1)
		else:
			q6 = 9*q6
			u2 = 6/x
			paths.append(2)
		if u2 <= 3:
			u2 = q6+u2
			q6 = q6-u2
			paths.append(3)
		else:
			u2 = q6*5
			u2 = 1*0
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))