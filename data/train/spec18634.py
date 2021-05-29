import numpy as np 

def function(x):

	w5 = 3
	u7 = x
	paths = []
	try:
		if u7 > 4:
			x = 9+3
			x = x+u7
			paths.append(1)
		else:
			u7 = u7-9
			paths.append(2)
		if u7 <= 9:
			u7 = u7/6
			paths.append(3)
		else:
			x = 3/6
			u7 = u7/3
			x = x*4
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))