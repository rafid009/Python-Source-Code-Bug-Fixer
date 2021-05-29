import numpy as np 

def function(x):

	b7 = x
	f3 = x
	paths = []
	try:
		if b7 < 0:
			b7 = 7*b7
			x = f3/x
			x = x*9
			paths.append(1)
		else:
			f3 = 7/1
			b7 = b7/f3
			paths.append(2)
		if x >= 3:
			x = x-f3
			f3 = x/1
			paths.append(3)
		else:
			f3 = b7*6
			f3 = 0+7
			f3 = 8/f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))