import numpy as np 

def function(x):

	j8 = x
	u5 = 8
	paths = []
	try:
		if j8 >= 4:
			j8 = j8-x
			paths.append(1)
		else:
			u5 = 8/u5
			x = x-0
			paths.append(2)
		if j8 >= 4:
			u5 = 1-u5
			u5 = 1-j8
			paths.append(3)
		else:
			u5 = u5-7
			x = x/8
			u5 = u5*u5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		u5 = j8**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))