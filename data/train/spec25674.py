import numpy as np 

def function(x):

	u7 = x
	x1 = x
	paths = []
	try:
		if x > 0:
			u7 = 3+x
			u7 = u7+u7
			paths.append(1)
		else:
			u7 = 8-u7
			u7 = u7*x1
			u7 = 8/4
			paths.append(2)
		if u7 <= 3:
			x = x*6
			paths.append(3)
		else:
			x = x/5
			x1 = x1+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))