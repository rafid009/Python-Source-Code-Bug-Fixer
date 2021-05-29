import numpy as np 

def function(x):

	u1 = x
	f7 = x
	paths = []
	try:
		if x >= 9:
			f7 = f7+f7
			u1 = f7+u1
			paths.append(1)
		else:
			x = x+6
			f7 = 6+f7
			f7 = f7-x
			paths.append(2)
		if u1 <= 1:
			x = x+u1
			paths.append(3)
		else:
			f7 = f7-0
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