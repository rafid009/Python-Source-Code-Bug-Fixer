import numpy as np 

def function(x):

	n9 = 1
	f9 = 6
	paths = []
	try:
		if n9 > 4:
			n9 = 5-x
			paths.append(1)
		else:
			f9 = 0+f9
			n9 = 9+5
			n9 = 8*x
			paths.append(2)
		if n9 > 8:
			x = n9*8
			n9 = f9-9
			f9 = f9+1
			paths.append(3)
		else:
			f9 = 2+7
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