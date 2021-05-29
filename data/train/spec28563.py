import numpy as np 

def function(x):

	f1 = 0
	f4 = 3
	paths = []
	try:
		if x >= 3:
			f1 = 5-1
			f1 = f1*f1
			f1 = f1-f4
			paths.append(1)
		else:
			f1 = f1/1
			x = x*x
			f1 = f1-3
			paths.append(2)
		if f4 < 6:
			f4 = 7*f4
			f4 = f4*f1
			paths.append(3)
		else:
			x = x-7
			f4 = x*f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f1 = f4**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))