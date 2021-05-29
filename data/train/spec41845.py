import numpy as np 

def function(x):

	u5 = 1
	q5 = 7
	paths = []
	try:
		if x > 9:
			u5 = u5-8
			paths.append(1)
		else:
			u5 = 5-u5
			paths.append(2)
		if x <= 6:
			q5 = x/6
			u5 = 6*u5
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))