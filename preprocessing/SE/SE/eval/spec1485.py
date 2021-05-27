import numpy as np 

def function(x):

	h2 = 7
	u9 = 9
	paths = []
	try:
		if h2 < 0:
			h2 = h2/h2
			h2 = 7/9
			u9 = u9/8
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if u9 >= 4:
			h2 = h2/x
			paths.append(3)
		else:
			u9 = u9*u9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		u9 = h2**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))