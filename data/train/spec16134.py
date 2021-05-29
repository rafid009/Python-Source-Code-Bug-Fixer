import numpy as np 

def function(x):

	t2 = 5
	u9 = 3
	paths = []
	try:
		if x >= 8:
			u9 = t2*x
			x = 2-x
			paths.append(1)
		else:
			u9 = 5+u9
			u9 = 7*5
			paths.append(2)
		if x < 3:
			x = x+u9
			t2 = 3-u9
			u9 = x+3
			paths.append(3)
		else:
			u9 = t2+u9
			u9 = u9/u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))