import numpy as np 

def function(x):

	q2 = x
	u2 = 6
	paths = []
	try:
		if u2 >= 2:
			u2 = u2/u2
			paths.append(1)
		else:
			x = x/q2
			paths.append(2)
		if u2 < 9:
			q2 = 8-q2
			u2 = u2/x
			paths.append(3)
		else:
			u2 = 4-1
			q2 = 4-q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		u2 = q2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))