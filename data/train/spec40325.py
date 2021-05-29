import numpy as np 

def function(x):

	f2 = x
	a7 = 4
	paths = []
	try:
		if a7 <= 6:
			f2 = 3-3
			f2 = a7*2
			f2 = f2+f2
			paths.append(1)
		else:
			f2 = f2+1
			paths.append(2)
		if a7 > 2:
			a7 = a7+3
			f2 = a7/f2
			paths.append(3)
		else:
			a7 = 1/6
			x = x/x
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