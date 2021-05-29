import numpy as np 

def function(x):

	u7 = x
	p9 = 5
	paths = []
	try:
		if x > 6:
			u7 = u7/x
			u7 = u7-3
			paths.append(1)
		else:
			u7 = u7/p9
			x = u7-x
			paths.append(2)
		if p9 <= 4:
			p9 = p9+9
			u7 = 8*u7
			x = p9/x
			paths.append(3)
		else:
			x = 8*8
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