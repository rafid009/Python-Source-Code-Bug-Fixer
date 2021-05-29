import numpy as np 

def function(x):

	q6 = 5
	u9 = x
	paths = []
	try:
		if u9 <= 6:
			u9 = u9*3
			paths.append(1)
		else:
			x = x*4
			q6 = x+7
			q6 = q6/4
			paths.append(2)
		if u9 <= 3:
			u9 = u9-2
			x = x*9
			q6 = 4-0
			paths.append(3)
		else:
			q6 = 5-x
			x = x/9
			u9 = q6*u9
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