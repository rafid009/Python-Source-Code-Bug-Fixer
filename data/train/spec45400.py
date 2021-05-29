import numpy as np 

def function(x):

	u7 = 1
	j4 = x
	paths = []
	try:
		if u7 < 0:
			j4 = j4/8
			paths.append(1)
		else:
			u7 = 3+5
			u7 = 8*u7
			u7 = 2-u7
			paths.append(2)
		if x > 0:
			x = 7+x
			j4 = j4+7
			u7 = x/5
			paths.append(3)
		else:
			u7 = 4/4
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