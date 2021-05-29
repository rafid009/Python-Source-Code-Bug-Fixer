import numpy as np 

def function(x):

	u7 = x
	h2 = x
	paths = []
	try:
		if x < 4:
			u7 = 7-9
			h2 = u7*x
			u7 = 6-u7
			paths.append(1)
		else:
			u7 = 3*h2
			x = u7+x
			u7 = u7-x
			paths.append(2)
		if x < 4:
			u7 = 1+3
			u7 = u7*u7
			paths.append(3)
		else:
			u7 = u7/h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		u7 = h2**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))