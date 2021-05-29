import numpy as np 

def function(x):

	f5 = x
	f4 = 0
	paths = []
	try:
		if x > 1:
			x = f4*1
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if f5 < 6:
			f5 = f5/4
			f5 = f4-9
			f5 = f5+f4
			paths.append(3)
		else:
			f5 = f5-4
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))