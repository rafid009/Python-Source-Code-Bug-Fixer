import numpy as np 

def function(x):

	a3 = 4
	u4 = x
	paths = []
	try:
		if u4 >= 6:
			a3 = u4/a3
			paths.append(1)
		else:
			x = x*1
			u4 = 4*u4
			paths.append(2)
		if x < 9:
			a3 = a3-x
			paths.append(3)
		else:
			u4 = u4-9
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		u4 = a3**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))