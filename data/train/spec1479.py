import numpy as np 

def function(x):

	j8 = 2
	u6 = 4
	x = 2
	paths = []
	try:
		if u6 > 6:
			j8 = j8/j8
			j8 = 9*j8
			u6 = j8/j8
			paths.append(1)
		else:
			j8 = j8-4
			x = x+x
			paths.append(2)
		if x >= 5:
			j8 = x-j8
			paths.append(3)
		else:
			x = 1/u6
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		u6 = j8**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))