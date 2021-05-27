import numpy as np 

def function(x):

	u7 = 9
	f5 = x
	paths = []
	try:
		if f5 <= 0:
			x = f5/f5
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if f5 <= 7:
			x = x+x
			paths.append(3)
		else:
			f5 = 0-6
			x = 7/2
			u7 = 0+x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		u7 = f5**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))