import numpy as np 

def function(x):

	f7 = 4
	u9 = 9
	paths = []
	try:
		if u9 < 8:
			x = x+3
			f7 = 9/x
			paths.append(1)
		else:
			u9 = 7/f7
			paths.append(2)
		if x >= 9:
			x = x-3
			x = x-1
			f7 = 3+7
			paths.append(3)
		else:
			u9 = u9+1
			x = 5+x
			u9 = u9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))