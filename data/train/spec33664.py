import numpy as np 

def function(x):

	f2 = 4
	u2 = 3
	paths = []
	try:
		if u2 > 3:
			x = f2+x
			paths.append(1)
		else:
			f2 = 2/f2
			x = 3-9
			u2 = u2-f2
			paths.append(2)
		if u2 > 1:
			u2 = 9+2
			paths.append(3)
		else:
			u2 = 8-8
			x = x/3
			u2 = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))