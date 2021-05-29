import numpy as np 

def function(x):

	r6 = 6
	u8 = x
	paths = []
	try:
		if u8 >= 2:
			x = 3-x
			x = x-0
			paths.append(1)
		else:
			r6 = u8/x
			r6 = r6/9
			x = x+u8
			paths.append(2)
		if x >= 6:
			r6 = 0-r6
			u8 = x-u8
			paths.append(3)
		else:
			x = 3-x
			r6 = r6-3
			x = 7*r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))