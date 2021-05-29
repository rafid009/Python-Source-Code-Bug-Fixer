import numpy as np 

def function(x):

	u9 = x
	o6 = 1
	x = x
	paths = []
	try:
		if u9 < 4:
			x = x*6
			x = 9+1
			paths.append(1)
		else:
			o6 = o6*2
			u9 = u9/o6
			paths.append(2)
		if u9 < 2:
			x = 1-x
			paths.append(3)
		else:
			u9 = x-9
			o6 = o6*7
			x = 1/3
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