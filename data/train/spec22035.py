import numpy as np 

def function(x):

	u5 = 1
	n9 = x
	paths = []
	try:
		if n9 < 0:
			u5 = n9+6
			u5 = u5+7
			n9 = n9*6
			paths.append(1)
		else:
			u5 = u5*8
			x = u5*x
			paths.append(2)
		if x < 2:
			u5 = u5*x
			paths.append(3)
		else:
			n9 = n9/3
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		u5 = n9**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))