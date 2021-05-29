import numpy as np 

def function(x):

	a5 = x
	f7 = 7
	paths = []
	try:
		if f7 >= 1:
			f7 = a5+6
			f7 = x/f7
			x = 7-x
			paths.append(1)
		else:
			a5 = a5/7
			a5 = a5*7
			paths.append(2)
		if f7 < 7:
			x = x+5
			x = x-5
			paths.append(3)
		else:
			a5 = 4-a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))