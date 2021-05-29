import numpy as np 

def function(x):

	a2 = 7
	f1 = 6
	paths = []
	try:
		if x <= 0:
			x = x-3
			paths.append(1)
		else:
			f1 = x+f1
			a2 = f1-0
			a2 = x+x
			paths.append(2)
		if f1 >= 1:
			f1 = 1-f1
			paths.append(3)
		else:
			x = a2/x
			f1 = f1/f1
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