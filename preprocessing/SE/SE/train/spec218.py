import numpy as np 

def function(x):

	u7 = 9
	f6 = 7
	paths = []
	try:
		if f6 <= 5:
			f6 = f6*8
			x = 6-x
			u7 = 8/3
			paths.append(1)
		else:
			u7 = u7+u7
			paths.append(2)
		if x >= 7:
			u7 = u7/x
			paths.append(3)
		else:
			f6 = f6*4
			u7 = 8*u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))