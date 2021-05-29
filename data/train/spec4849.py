import numpy as np 

def function(x):

	f6 = x
	a3 = x
	x = 9
	paths = []
	try:
		if f6 <= 9:
			f6 = f6+8
			a3 = a3*x
			x = f6-f6
			paths.append(1)
		else:
			a3 = x+6
			x = x+5
			paths.append(2)
		if a3 < 5:
			a3 = 8/7
			paths.append(3)
		else:
			x = x-a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))