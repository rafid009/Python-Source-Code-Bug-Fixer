import numpy as np 

def function(x):

	u9 = 7
	y5 = 9
	paths = []
	try:
		if x <= 8:
			x = x/7
			u9 = x*5
			y5 = y5+y5
			paths.append(1)
		else:
			u9 = 8+9
			paths.append(2)
		if u9 > 2:
			x = 1/7
			u9 = u9-3
			x = 2+1
			paths.append(3)
		else:
			u9 = u9-7
			y5 = 3-y5
			u9 = u9*y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))