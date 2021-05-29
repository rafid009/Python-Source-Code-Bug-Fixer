import numpy as np 

def function(x):

	q7 = 4
	u5 = 2
	paths = []
	try:
		if q7 <= 8:
			q7 = 5+q7
			q7 = q7*1
			paths.append(1)
		else:
			u5 = 8+u5
			paths.append(2)
		if u5 <= 0:
			x = 6/4
			q7 = u5/4
			paths.append(3)
		else:
			q7 = q7+0
			x = 7*x
			u5 = 3/q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))