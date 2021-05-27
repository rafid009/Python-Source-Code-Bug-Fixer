import numpy as np 

def function(x):

	a8 = 5
	f3 = x
	paths = []
	try:
		if a8 > 8:
			f3 = f3-0
			f3 = 6/f3
			paths.append(1)
		else:
			f3 = f3*3
			a8 = x+x
			paths.append(2)
		if a8 <= 1:
			a8 = a8*9
			x = f3*x
			f3 = f3/f3
			paths.append(3)
		else:
			a8 = f3*0
			x = x-8
			f3 = 5-f3
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