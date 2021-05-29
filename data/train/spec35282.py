import numpy as np 

def function(x):

	u5 = 8
	f2 = 2
	paths = []
	try:
		if u5 <= 2:
			u5 = x-2
			paths.append(1)
		else:
			f2 = f2-9
			f2 = f2+u5
			paths.append(2)
		if u5 <= 7:
			u5 = 0+9
			x = 8/x
			f2 = u5-4
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))