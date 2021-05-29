import numpy as np 

def function(x):

	f7 = 6
	f4 = 9
	paths = []
	try:
		if x <= 9:
			f4 = f4/f7
			f7 = f7*x
			paths.append(1)
		else:
			x = x/8
			f4 = f7*f4
			paths.append(2)
		if x < 2:
			x = 6+7
			paths.append(3)
		else:
			f7 = 3+6
			x = x-4
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f4 = f7**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))