import numpy as np 

def function(x):

	a6 = x
	b5 = x
	paths = []
	try:
		if a6 < 4:
			a6 = a6-5
			x = 4*x
			paths.append(1)
		else:
			x = x*7
			b5 = 2-b5
			b5 = b5/b5
			paths.append(2)
		if x <= 8:
			a6 = a6/a6
			a6 = 8-a6
			paths.append(3)
		else:
			x = x-0
			a6 = 7/a6
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		a6 = b5**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))