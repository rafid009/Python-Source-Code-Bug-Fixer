import numpy as np 

def function(x):

	x5 = 4
	f1 = x
	paths = []
	try:
		if x >= 3:
			x5 = x5*8
			f1 = f1/9
			f1 = f1*x5
			paths.append(1)
		else:
			x = 7/x
			x = x+6
			x5 = x5*5
			paths.append(2)
		if x5 >= 8:
			f1 = f1/9
			x5 = 0+x5
			paths.append(3)
		else:
			x5 = x5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))