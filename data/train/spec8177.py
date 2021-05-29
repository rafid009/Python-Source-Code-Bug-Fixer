import numpy as np 

def function(x):

	q1 = 7
	u5 = 4
	paths = []
	try:
		if x > 2:
			q1 = u5/q1
			x = x-5
			x = q1-q1
			paths.append(1)
		else:
			q1 = x+q1
			u5 = 8-u5
			x = q1-x
			paths.append(2)
		if u5 >= 4:
			x = x-3
			paths.append(3)
		else:
			q1 = 1-x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))