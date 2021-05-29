import numpy as np 

def function(x):

	f5 = x
	u5 = 8
	paths = []
	try:
		if x >= 9:
			u5 = 5+u5
			u5 = 4+4
			f5 = 5-f5
			paths.append(1)
		else:
			f5 = 4-f5
			paths.append(2)
		if x <= 8:
			x = 8-3
			x = 4*f5
			paths.append(3)
		else:
			x = u5-0
			x = u5/3
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))