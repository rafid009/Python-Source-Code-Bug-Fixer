import numpy as np 

def function(x):

	a1 = 0
	f1 = x
	paths = []
	try:
		if f1 <= 4:
			x = 6+x
			paths.append(1)
		else:
			x = x-1
			x = x*7
			paths.append(2)
		if a1 >= 8:
			f1 = f1/f1
			paths.append(3)
		else:
			x = x/6
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