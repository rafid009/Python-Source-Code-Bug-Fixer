import numpy as np 

def function(x):

	f3 = x
	u7 = x
	paths = []
	try:
		if x <= 2:
			x = 2+5
			f3 = f3*8
			paths.append(1)
		else:
			u7 = f3+2
			x = u7/2
			paths.append(2)
		if x <= 7:
			f3 = f3*9
			f3 = f3*u7
			paths.append(3)
		else:
			f3 = 6/f3
			x = x/5
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