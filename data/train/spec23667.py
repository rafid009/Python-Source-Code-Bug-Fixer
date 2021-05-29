import numpy as np 

def function(x):

	f4 = x
	k5 = x
	paths = []
	try:
		if f4 > 4:
			x = x*9
			x = 5+2
			paths.append(1)
		else:
			f4 = f4-4
			f4 = 5*f4
			k5 = 1/5
			paths.append(2)
		if f4 >= 1:
			f4 = 6/f4
			f4 = f4-0
			paths.append(3)
		else:
			k5 = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))