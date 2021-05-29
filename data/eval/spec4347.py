import numpy as np 

def function(x):

	u9 = x
	n1 = x
	paths = []
	try:
		if x > 3:
			u9 = 2-u9
			u9 = u9*9
			paths.append(1)
		else:
			u9 = 9+u9
			n1 = n1+6
			n1 = x-n1
			paths.append(2)
		if u9 < 1:
			x = x-9
			paths.append(3)
		else:
			x = 1*u9
			u9 = 8-n1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))