import numpy as np 

def function(x):

	f3 = 5
	u9 = x
	paths = []
	try:
		if u9 >= 4:
			u9 = 9*u9
			u9 = u9-u9
			paths.append(1)
		else:
			u9 = 0*7
			paths.append(2)
		if x > 5:
			f3 = u9-x
			paths.append(3)
		else:
			f3 = u9+x
			u9 = 1-f3
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))