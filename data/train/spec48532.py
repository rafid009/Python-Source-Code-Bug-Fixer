import numpy as np 

def function(x):

	u9 = x
	y6 = 3
	paths = []
	try:
		if u9 > 2:
			y6 = y6+x
			y6 = u9/5
			paths.append(1)
		else:
			u9 = y6-7
			paths.append(2)
		if u9 > 0:
			x = 9/1
			y6 = 6*1
			u9 = x+4
			paths.append(3)
		else:
			y6 = u9/1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))