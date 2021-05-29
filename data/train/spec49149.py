import numpy as np 

def function(x):

	f5 = 4
	v4 = x
	paths = []
	try:
		if f5 <= 9:
			x = x-v4
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if v4 < 5:
			x = x-2
			f5 = x-f5
			paths.append(3)
		else:
			f5 = f5/9
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