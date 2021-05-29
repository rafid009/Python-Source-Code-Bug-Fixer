import numpy as np 

def function(x):

	x1 = 8
	f0 = x
	paths = []
	try:
		if x1 <= 9:
			x = x-5
			x1 = 0*x
			x1 = x1*x1
			paths.append(1)
		else:
			x = 6*x
			x1 = 0/2
			paths.append(2)
		if f0 <= 1:
			x1 = x1-x
			x1 = x1+x
			x1 = x1-9
			paths.append(3)
		else:
			f0 = 9*x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		f0 = x1**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))