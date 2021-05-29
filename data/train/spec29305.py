import numpy as np 

def function(x):

	f7 = x
	u9 = 6
	paths = []
	try:
		if f7 > 6:
			x = x+5
			u9 = u9*9
			u9 = u9-4
			paths.append(1)
		else:
			x = x+0
			x = x-0
			paths.append(2)
		if u9 < 3:
			u9 = x/8
			u9 = u9*4
			paths.append(3)
		else:
			u9 = 8*3
			x = f7*1
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