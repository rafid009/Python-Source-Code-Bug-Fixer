import numpy as np 

def function(x):

	n4 = x
	u7 = x
	paths = []
	try:
		if u7 >= 4:
			x = 4*x
			paths.append(1)
		else:
			u7 = x/5
			u7 = x*7
			u7 = u7-0
			paths.append(2)
		if x < 8:
			x = x-8
			u7 = u7+4
			paths.append(3)
		else:
			u7 = u7-u7
			u7 = u7*8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		u7 = n4**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))