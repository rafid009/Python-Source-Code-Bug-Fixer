import numpy as np 

def function(x):

	f3 = 5
	a7 = x
	paths = []
	try:
		if x >= 5:
			x = x-f3
			f3 = f3-f3
			paths.append(1)
		else:
			x = x*3
			x = x-5
			paths.append(2)
		if a7 >= 1:
			f3 = 6-1
			a7 = 3/x
			paths.append(3)
		else:
			f3 = 2+f3
			f3 = 7/f3
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))