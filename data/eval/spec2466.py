import numpy as np 

def function(x):

	l7 = 0
	u5 = x
	paths = []
	try:
		if u5 <= 3:
			x = x+4
			x = u5-x
			paths.append(1)
		else:
			u5 = u5+u5
			paths.append(2)
		if x >= 3:
			l7 = x+5
			l7 = 7+3
			x = 5-3
			paths.append(3)
		else:
			u5 = u5*3
			u5 = u5-7
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