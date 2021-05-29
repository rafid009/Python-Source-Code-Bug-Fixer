import numpy as np 

def function(x):

	f1 = 5
	a8 = x
	paths = []
	try:
		if f1 <= 5:
			a8 = f1+8
			a8 = 2*f1
			a8 = f1-a8
			paths.append(1)
		else:
			x = x+a8
			f1 = f1-1
			x = 5/3
			paths.append(2)
		if x >= 2:
			x = 3-7
			a8 = x-a8
			f1 = a8*x
			paths.append(3)
		else:
			x = 3-x
			x = x+3
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		f1 = a8**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))