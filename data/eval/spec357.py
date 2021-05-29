import numpy as np 

def function(x):

	v1 = x
	u5 = x
	paths = []
	try:
		if x >= 2:
			v1 = x+v1
			paths.append(1)
		else:
			x = 3+x
			x = 9-6
			paths.append(2)
		if v1 > 9:
			x = x+v1
			x = v1/x
			paths.append(3)
		else:
			u5 = 7*u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		v1 = u5**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))