import numpy as np 

def function(x):

	n7 = x
	u7 = x
	paths = []
	try:
		if u7 <= 7:
			u7 = u7*u7
			x = x-n7
			paths.append(1)
		else:
			u7 = u7/7
			x = 1*1
			paths.append(2)
		if n7 >= 0:
			x = x*8
			paths.append(3)
		else:
			x = u7+x
			u7 = 8-x
			x = x+n7
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