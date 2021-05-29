import numpy as np 

def function(x):

	f0 = 3
	u7 = 0
	x = 4
	paths = []
	try:
		if x > 7:
			f0 = f0/9
			paths.append(1)
		else:
			u7 = 2+4
			u7 = 9*7
			paths.append(2)
		if u7 > 4:
			u7 = 0-5
			u7 = 2/u7
			u7 = u7/f0
			paths.append(3)
		else:
			f0 = f0*9
			f0 = f0+9
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