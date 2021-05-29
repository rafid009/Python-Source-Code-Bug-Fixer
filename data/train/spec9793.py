import numpy as np 

def function(x):

	u4 = x
	o4 = x
	paths = []
	try:
		if x >= 8:
			u4 = u4+3
			u4 = 3*u4
			o4 = x+x
			paths.append(1)
		else:
			x = x*6
			o4 = 3+o4
			paths.append(2)
		if u4 <= 7:
			u4 = u4/x
			paths.append(3)
		else:
			x = u4+u4
			o4 = x+o4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))