import numpy as np 

def function(x):

	u7 = x
	f9 = 0
	paths = []
	try:
		if f9 > 2:
			u7 = u7-f9
			u7 = u7*8
			u7 = 3+3
			paths.append(1)
		else:
			x = u7+4
			x = x*1
			paths.append(2)
		if f9 < 0:
			f9 = f9*f9
			paths.append(3)
		else:
			f9 = 2+f9
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