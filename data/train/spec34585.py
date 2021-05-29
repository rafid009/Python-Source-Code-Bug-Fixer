import numpy as np 

def function(x):

	f2 = x
	u2 = 2
	paths = []
	try:
		if u2 < 9:
			f2 = 4-f2
			paths.append(1)
		else:
			f2 = f2+4
			x = f2+x
			paths.append(2)
		if f2 < 9:
			u2 = u2/x
			paths.append(3)
		else:
			x = x/3
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