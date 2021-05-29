import numpy as np 

def function(x):

	n1 = x
	f6 = 5
	paths = []
	try:
		if x >= 6:
			n1 = f6*x
			f6 = 1*f6
			f6 = f6+f6
			paths.append(1)
		else:
			n1 = n1*3
			x = 1-4
			f6 = f6-4
			paths.append(2)
		if n1 <= 4:
			n1 = 8*5
			f6 = 0*f6
			paths.append(3)
		else:
			x = f6/x
			x = 7/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))