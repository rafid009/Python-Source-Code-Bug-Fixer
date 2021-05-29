import numpy as np 

def function(x):

	u6 = x
	q5 = x
	paths = []
	try:
		if u6 <= 6:
			q5 = 2+0
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x < 8:
			u6 = u6-7
			paths.append(3)
		else:
			x = 9/q5
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