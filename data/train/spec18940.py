import numpy as np 

def function(x):

	u5 = x
	u9 = 8
	paths = []
	try:
		if u9 > 8:
			u5 = u9-u5
			u5 = 1*u5
			u5 = 7+x
			paths.append(1)
		else:
			u5 = 1*u5
			x = x*u9
			u9 = 7+x
			paths.append(2)
		if u5 < 4:
			x = x*2
			u5 = 3+u5
			u9 = x*u5
			paths.append(3)
		else:
			x = 6/x
			u5 = u5/u9
			x = x+7
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))