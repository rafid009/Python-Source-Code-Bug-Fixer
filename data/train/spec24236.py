import numpy as np 

def function(x):

	f2 = 4
	a7 = x
	paths = []
	try:
		if a7 > 1:
			a7 = a7-f2
			f2 = x-f2
			paths.append(1)
		else:
			x = f2+x
			f2 = f2-5
			f2 = f2/9
			paths.append(2)
		if a7 <= 7:
			f2 = f2/9
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))