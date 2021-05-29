import numpy as np 

def function(x):

	u7 = x
	a6 = x
	paths = []
	try:
		if u7 >= 3:
			u7 = 0/a6
			paths.append(1)
		else:
			x = x-0
			u7 = u7+3
			x = 4+x
			paths.append(2)
		if u7 > 7:
			x = a6+x
			x = x-6
			paths.append(3)
		else:
			u7 = u7-9
			a6 = a6+0
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