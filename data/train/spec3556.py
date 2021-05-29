import numpy as np 

def function(x):

	a9 = 8
	f6 = 6
	paths = []
	try:
		if x > 9:
			f6 = f6-1
			x = x-8
			paths.append(1)
		else:
			a9 = 1-8
			f6 = a9-f6
			x = 1/x
			paths.append(2)
		if f6 < 7:
			f6 = 3*9
			x = x+6
			f6 = f6+4
			paths.append(3)
		else:
			a9 = a9*f6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))