import numpy as np 

def function(x):

	v1 = x
	u7 = x
	paths = []
	try:
		if x < 1:
			v1 = v1-2
			paths.append(1)
		else:
			x = x+v1
			v1 = 5+3
			u7 = u7+v1
			paths.append(2)
		if u7 > 5:
			x = 3/7
			v1 = v1-x
			v1 = x*v1
			paths.append(3)
		else:
			u7 = 0+v1
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))