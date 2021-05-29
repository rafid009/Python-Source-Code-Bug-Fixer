import numpy as np 

def function(x):

	f5 = 8
	a0 = x
	paths = []
	try:
		if a0 < 7:
			a0 = a0/2
			x = 9+x
			a0 = a0+8
			paths.append(1)
		else:
			a0 = x-a0
			paths.append(2)
		if a0 >= 4:
			x = x/f5
			x = 7/2
			a0 = x+5
			paths.append(3)
		else:
			x = x-6
			x = 1/x
			f5 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))