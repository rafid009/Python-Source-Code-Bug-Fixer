import numpy as np 

def function(x):

	u5 = x
	y4 = x
	paths = []
	try:
		if x < 9:
			y4 = 9/5
			paths.append(1)
		else:
			x = x*y4
			x = u5*x
			u5 = 7/5
			paths.append(2)
		if y4 >= 4:
			y4 = y4+1
			paths.append(3)
		else:
			y4 = x*8
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))