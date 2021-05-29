import numpy as np 

def function(x):

	f3 = 1
	f5 = 9
	paths = []
	try:
		if f5 >= 3:
			f3 = x/f3
			paths.append(1)
		else:
			f5 = f5-5
			paths.append(2)
		if f3 < 6:
			f3 = 3+f3
			f5 = f5*9
			x = 8*x
			paths.append(3)
		else:
			f5 = f5-f5
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