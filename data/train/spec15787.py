import numpy as np 

def function(x):

	u9 = 5
	f6 = 1
	paths = []
	try:
		if f6 > 3:
			x = f6/u9
			f6 = u9-8
			paths.append(1)
		else:
			f6 = x/f6
			f6 = f6/6
			paths.append(2)
		if x > 4:
			x = x+7
			x = 0*5
			u9 = 7/2
			paths.append(3)
		else:
			u9 = f6/5
			f6 = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))