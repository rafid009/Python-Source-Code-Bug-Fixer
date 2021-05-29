import numpy as np 

def function(x):

	u7 = x
	e9 = x
	paths = []
	try:
		if u7 >= 2:
			x = x+3
			paths.append(1)
		else:
			e9 = e9/7
			x = x*1
			x = x-5
			paths.append(2)
		if e9 > 7:
			x = x-x
			u7 = u7-8
			u7 = e9-5
			paths.append(3)
		else:
			x = x-1
			e9 = e9*7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		e9 = u7**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))