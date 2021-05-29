import numpy as np 

def function(x):

	v7 = 8
	u1 = x
	paths = []
	try:
		if x <= 0:
			x = 7+v7
			x = 5*x
			v7 = 2+4
			paths.append(1)
		else:
			u1 = 0-x
			paths.append(2)
		if u1 >= 9:
			x = x*7
			x = u1-x
			paths.append(3)
		else:
			v7 = u1*v7
			x = 1-x
			x = x/3
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		u1 = v7**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))