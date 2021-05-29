import numpy as np 

def function(x):

	f1 = 3
	f0 = x
	x = x
	paths = []
	try:
		if f0 >= 8:
			f0 = f0*x
			f1 = 9+9
			paths.append(1)
		else:
			f1 = f0/f1
			f1 = f1-9
			paths.append(2)
		if x >= 5:
			f1 = f1*f1
			f0 = 5/f0
			f1 = f1/1
			paths.append(3)
		else:
			f1 = 6*f1
			x = x/8
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f1 = f0**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))