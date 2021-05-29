import numpy as np 

def function(x):

	y4 = 7
	u5 = x
	paths = []
	try:
		if y4 <= 1:
			u5 = 1-u5
			u5 = 3+5
			x = y4+x
			paths.append(1)
		else:
			x = 8/7
			x = x+2
			x = x-u5
			paths.append(2)
		if u5 <= 6:
			u5 = x/4
			paths.append(3)
		else:
			y4 = y4/y4
			x = y4*0
			u5 = u5/7
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