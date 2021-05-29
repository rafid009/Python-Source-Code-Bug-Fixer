import numpy as np 

def function(x):

	u4 = 8
	y3 = 5
	paths = []
	try:
		if x <= 7:
			u4 = 5-u4
			u4 = y3-6
			x = 7+x
			paths.append(1)
		else:
			x = x*7
			y3 = u4/x
			u4 = u4/y3
			paths.append(2)
		if u4 > 1:
			y3 = y3+x
			y3 = 7*u4
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		y3 = u4**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))