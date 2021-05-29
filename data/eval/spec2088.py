import numpy as np 

def function(x):

	v4 = x
	f0 = 7
	paths = []
	try:
		if v4 <= 0:
			x = v4-x
			x = 5*1
			f0 = 6-f0
			paths.append(1)
		else:
			f0 = 4-1
			v4 = 8*6
			paths.append(2)
		if x > 0:
			v4 = v4/1
			v4 = 1/v4
			x = 9*5
			paths.append(3)
		else:
			v4 = 9*6
			x = 4-v4
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))