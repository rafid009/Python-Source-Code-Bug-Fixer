import numpy as np 

def function(x):

	k4 = x
	f7 = 1
	paths = []
	try:
		if k4 < 2:
			f7 = 5*1
			k4 = k4-1
			paths.append(1)
		else:
			f7 = 1-3
			paths.append(2)
		if k4 <= 3:
			k4 = 9+k4
			x = x+8
			f7 = f7/8
			paths.append(3)
		else:
			x = k4/7
			k4 = 5/k4
			k4 = k4*1
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		k4 = f7**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))