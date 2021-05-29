import numpy as np 

def function(x):

	u7 = 3
	f1 = x
	paths = []
	try:
		if x <= 1:
			x = 2+x
			paths.append(1)
		else:
			x = 2+0
			u7 = u7-u7
			x = x-f1
			paths.append(2)
		if f1 > 1:
			f1 = 3/f1
			x = f1/x
			u7 = 7/1
			paths.append(3)
		else:
			x = x+0
			u7 = f1/x
			u7 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))