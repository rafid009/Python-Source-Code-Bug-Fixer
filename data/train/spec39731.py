import numpy as np 

def function(x):

	u7 = 1
	b1 = x
	paths = []
	try:
		if x <= 0:
			x = x*1
			paths.append(1)
		else:
			x = x*8
			u7 = 5*u7
			x = 2-7
			paths.append(2)
		if x >= 2:
			b1 = 5-b1
			paths.append(3)
		else:
			x = 3-5
			u7 = u7+0
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