import numpy as np 

def function(x):

	u2 = 1
	x1 = 5
	paths = []
	try:
		if u2 <= 5:
			x1 = 5+9
			x1 = x1*3
			u2 = x+u2
			paths.append(1)
		else:
			x = 1/x
			x = 8+x
			x1 = 0+9
			paths.append(2)
		if x < 6:
			x1 = u2-x1
			x = x*x
			paths.append(3)
		else:
			u2 = x1-u2
			x1 = x1*7
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))