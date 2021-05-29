import numpy as np 

def function(x):

	a8 = 8
	f8 = 4
	paths = []
	try:
		if f8 > 5:
			x = f8+4
			a8 = a8/x
			f8 = 7*9
			paths.append(1)
		else:
			f8 = 3+f8
			paths.append(2)
		if x <= 5:
			a8 = 4/a8
			x = x-2
			paths.append(3)
		else:
			x = x-x
			f8 = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))