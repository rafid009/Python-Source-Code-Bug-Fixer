import numpy as np 

def function(x):

	u2 = x
	q4 = x
	paths = []
	try:
		if x <= 5:
			x = 0/2
			paths.append(1)
		else:
			u2 = 4/u2
			q4 = 2/u2
			paths.append(2)
		if q4 <= 6:
			u2 = u2*2
			x = 6*9
			paths.append(3)
		else:
			u2 = u2*9
			q4 = q4/q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))