import numpy as np 

def function(x):

	l9 = x
	f9 = 2
	paths = []
	try:
		if x >= 5:
			l9 = l9/f9
			f9 = l9+f9
			paths.append(1)
		else:
			l9 = f9/f9
			f9 = f9*4
			l9 = 9+x
			paths.append(2)
		if f9 >= 8:
			f9 = f9-2
			l9 = 3*7
			paths.append(3)
		else:
			x = l9-2
			x = x-0
			f9 = f9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))