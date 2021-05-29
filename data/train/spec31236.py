import numpy as np 

def function(x):

	u5 = 8
	y4 = 5
	paths = []
	try:
		if x >= 1:
			y4 = x+5
			u5 = u5-2
			y4 = 5/6
			paths.append(1)
		else:
			u5 = 2-u5
			y4 = y4/2
			u5 = u5-7
			paths.append(2)
		if y4 <= 4:
			x = 9/y4
			u5 = 3-x
			paths.append(3)
		else:
			y4 = y4*1
			u5 = x+6
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		y4 = u5**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))