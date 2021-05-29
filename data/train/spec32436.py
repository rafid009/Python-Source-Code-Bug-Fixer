import numpy as np 

def function(x):

	q8 = x
	u7 = 5
	paths = []
	try:
		if x <= 0:
			x = u7+x
			q8 = 6*x
			paths.append(1)
		else:
			q8 = 8/q8
			u7 = 7*1
			x = x*6
			paths.append(2)
		if q8 <= 5:
			u7 = u7+9
			u7 = q8+q8
			paths.append(3)
		else:
			x = x+3
			q8 = q8-2
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))