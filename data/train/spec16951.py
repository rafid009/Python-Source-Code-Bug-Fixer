import numpy as np 

def function(x):

	l1 = 6
	u0 = 8
	paths = []
	try:
		if x > 9:
			u0 = l1/u0
			l1 = 3/l1
			paths.append(1)
		else:
			l1 = l1-2
			paths.append(2)
		if u0 >= 4:
			x = 8/l1
			u0 = 1+u0
			paths.append(3)
		else:
			x = 2-7
			u0 = u0+9
			l1 = 3-l1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))