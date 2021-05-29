import numpy as np 

def function(x):

	f1 = x
	u7 = x
	paths = []
	try:
		if f1 <= 6:
			x = 3+3
			paths.append(1)
		else:
			x = 0-6
			paths.append(2)
		if f1 <= 1:
			f1 = 3+u7
			f1 = f1*6
			paths.append(3)
		else:
			u7 = 2*u7
			f1 = f1/7
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		u7 = f1**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))