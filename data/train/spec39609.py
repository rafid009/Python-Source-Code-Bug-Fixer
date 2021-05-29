import numpy as np 

def function(x):

	u5 = x
	e9 = x
	paths = []
	try:
		if u5 < 9:
			u5 = u5*u5
			paths.append(1)
		else:
			e9 = e9+5
			e9 = 4-e9
			paths.append(2)
		if e9 >= 2:
			u5 = u5*1
			u5 = 4*6
			paths.append(3)
		else:
			u5 = 7+u5
			u5 = u5/8
			u5 = u5-e9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))