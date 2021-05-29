import numpy as np 

def function(x):

	a9 = x
	f7 = x
	paths = []
	try:
		if x >= 3:
			a9 = a9-x
			paths.append(1)
		else:
			x = 0+7
			a9 = a9-9
			paths.append(2)
		if f7 >= 9:
			a9 = 4-5
			f7 = f7*7
			f7 = 7/9
			paths.append(3)
		else:
			f7 = 3-f7
			x = x-5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))