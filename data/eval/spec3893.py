import numpy as np 

def function(x):

	y4 = 4
	u6 = x
	x = 9
	paths = []
	try:
		if u6 < 3:
			y4 = 2+3
			x = x+u6
			u6 = u6-8
			paths.append(1)
		else:
			y4 = y4+5
			u6 = 0*9
			paths.append(2)
		if u6 < 5:
			x = x/3
			y4 = 9-y4
			paths.append(3)
		else:
			y4 = 1+y4
			x = 5-x
			u6 = u6+6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		y4 = u6**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))