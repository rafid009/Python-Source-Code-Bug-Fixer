import numpy as np 

def function(x):

	u9 = x
	n8 = 6
	paths = []
	try:
		if x < 6:
			u9 = 4+u9
			u9 = n8*2
			paths.append(1)
		else:
			x = 9+x
			n8 = 4+n8
			n8 = n8+6
			paths.append(2)
		if n8 < 3:
			x = x+9
			u9 = 2/u9
			n8 = 1/n8
			paths.append(3)
		else:
			u9 = 3-6
			n8 = x-6
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