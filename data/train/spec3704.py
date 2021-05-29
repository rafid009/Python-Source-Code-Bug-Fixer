import numpy as np 

def function(x):

	f2 = 5
	f6 = x
	paths = []
	try:
		if f2 <= 6:
			f2 = 1/8
			f2 = f2/f2
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if f6 <= 5:
			x = 5*x
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))