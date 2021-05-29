import numpy as np 

def function(x):

	u9 = 7
	a0 = 0
	paths = []
	try:
		if u9 < 9:
			u9 = 4-u9
			a0 = a0-1
			x = u9/x
			paths.append(1)
		else:
			x = x+5
			x = x+x
			paths.append(2)
		if u9 > 6:
			u9 = 9/x
			u9 = u9/3
			paths.append(3)
		else:
			x = x-7
			a0 = a0-3
			x = a0/5
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