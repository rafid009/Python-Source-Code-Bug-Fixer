import numpy as np 

def function(x):

	v2 = 4
	u5 = 1
	paths = []
	try:
		if x <= 3:
			x = 5*x
			v2 = v2-2
			u5 = u5-u5
			paths.append(1)
		else:
			u5 = v2+v2
			v2 = 2-6
			v2 = v2+9
			paths.append(2)
		if x <= 3:
			u5 = v2-3
			paths.append(3)
		else:
			v2 = 8/v2
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