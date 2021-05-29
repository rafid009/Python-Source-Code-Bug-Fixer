import numpy as np 

def function(x):

	u9 = x
	q0 = x
	paths = []
	try:
		if q0 > 9:
			u9 = u9/7
			x = q0-7
			paths.append(1)
		else:
			q0 = q0-6
			x = 7*2
			u9 = 4-0
			paths.append(2)
		if u9 >= 7:
			x = x-x
			x = x+u9
			paths.append(3)
		else:
			x = x-9
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