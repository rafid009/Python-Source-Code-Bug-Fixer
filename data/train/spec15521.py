import numpy as np 

def function(x):

	j4 = x
	u7 = 5
	paths = []
	try:
		if j4 >= 6:
			u7 = x*5
			j4 = j4/u7
			j4 = j4*5
			paths.append(1)
		else:
			j4 = 5/j4
			x = x+4
			paths.append(2)
		if u7 > 7:
			j4 = j4+7
			u7 = 6-u7
			paths.append(3)
		else:
			x = 8*j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))