import numpy as np 

def function(x):

	f5 = x
	a6 = 3
	paths = []
	try:
		if a6 > 0:
			x = 2-4
			a6 = 5*2
			a6 = a6-8
			paths.append(1)
		else:
			f5 = 6-1
			x = a6/5
			a6 = 9-a6
			paths.append(2)
		if x <= 9:
			f5 = a6+a6
			paths.append(3)
		else:
			a6 = 9*6
			f5 = 0+f5
			f5 = f5*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))