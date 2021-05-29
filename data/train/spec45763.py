import numpy as np 

def function(x):

	w0 = 5
	f1 = 3
	paths = []
	try:
		if f1 >= 9:
			x = x*x
			f1 = f1*7
			paths.append(1)
		else:
			f1 = f1*x
			f1 = f1/4
			f1 = 2+3
			paths.append(2)
		if x <= 6:
			f1 = f1/6
			paths.append(3)
		else:
			x = 6*0
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