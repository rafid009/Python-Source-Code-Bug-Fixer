import numpy as np 

def function(x):

	u5 = x
	y1 = 7
	paths = []
	try:
		if y1 < 6:
			y1 = 0*2
			x = 3-x
			paths.append(1)
		else:
			x = y1*x
			u5 = 7-u5
			paths.append(2)
		if y1 >= 7:
			u5 = x/u5
			paths.append(3)
		else:
			u5 = 3-y1
			x = x+9
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