import numpy as np 

def function(x):

	u1 = 3
	q1 = x
	paths = []
	try:
		if q1 <= 5:
			u1 = u1-6
			u1 = u1/2
			paths.append(1)
		else:
			x = q1*3
			paths.append(2)
		if q1 < 8:
			u1 = q1-q1
			u1 = u1-6
			q1 = q1/x
			paths.append(3)
		else:
			u1 = u1*8
			x = x-x
			u1 = 9+u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))