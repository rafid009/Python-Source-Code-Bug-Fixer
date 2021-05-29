import numpy as np 

def function(x):

	u6 = 5
	e3 = 3
	paths = []
	try:
		if u6 <= 9:
			e3 = x/u6
			paths.append(1)
		else:
			u6 = u6+9
			paths.append(2)
		if x < 9:
			u6 = u6-x
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))