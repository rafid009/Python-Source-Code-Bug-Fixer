import numpy as np 

def function(x):

	q8 = 3
	f2 = 2
	paths = []
	try:
		if f2 <= 1:
			f2 = 7+f2
			f2 = 1*f2
			q8 = 6-4
			paths.append(1)
		else:
			x = x/f2
			x = x*7
			q8 = 0+6
			paths.append(2)
		if f2 > 9:
			x = x*f2
			paths.append(3)
		else:
			q8 = 9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))