import numpy as np 

def function(x):

	u9 = x
	v4 = x
	paths = []
	try:
		if v4 <= 0:
			v4 = v4+7
			u9 = 9-7
			u9 = u9/5
			paths.append(1)
		else:
			u9 = 7/u9
			paths.append(2)
		if v4 > 4:
			v4 = v4*7
			paths.append(3)
		else:
			x = u9-2
			u9 = 8/u9
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		u9 = v4**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))