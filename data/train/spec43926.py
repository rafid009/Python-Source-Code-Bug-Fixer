import numpy as np 

def function(x):

	u9 = 5
	u7 = x
	paths = []
	try:
		if x > 4:
			x = x/u9
			paths.append(1)
		else:
			u9 = 7*9
			u9 = u9*4
			paths.append(2)
		if u9 <= 9:
			x = 6+x
			x = 1-u7
			paths.append(3)
		else:
			x = 1+x
			x = x+2
			x = u7/u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))