import numpy as np 

def function(x):

	f5 = x
	u9 = 9
	paths = []
	try:
		if x >= 1:
			x = 5+x
			paths.append(1)
		else:
			u9 = u9*f5
			paths.append(2)
		if f5 >= 6:
			f5 = f5/9
			paths.append(3)
		else:
			x = 3*x
			x = 9/6
			f5 = u9-f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))