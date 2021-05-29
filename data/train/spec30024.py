import numpy as np 

def function(x):

	u1 = 8
	x2 = x
	paths = []
	try:
		if x <= 5:
			x2 = x2+x2
			x2 = x2/6
			paths.append(1)
		else:
			u1 = 8+u1
			u1 = 4/7
			x = 9+x
			paths.append(2)
		if u1 < 2:
			u1 = 7-0
			u1 = 6+8
			paths.append(3)
		else:
			x2 = 7+x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))