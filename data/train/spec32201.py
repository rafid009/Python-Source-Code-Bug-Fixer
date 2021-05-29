import numpy as np 

def function(x):

	u4 = x
	v8 = x
	paths = []
	try:
		if u4 <= 6:
			u4 = 9+8
			x = x*u4
			paths.append(1)
		else:
			x = 5/x
			x = x*5
			v8 = u4/4
			paths.append(2)
		if v8 < 2:
			v8 = u4+5
			x = x-2
			paths.append(3)
		else:
			x = x+v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))