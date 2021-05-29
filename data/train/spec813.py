import numpy as np 

def function(x):

	w8 = x
	f7 = 8
	paths = []
	try:
		if x <= 6:
			x = x-4
			f7 = x*f7
			paths.append(1)
		else:
			x = x-8
			f7 = 5*3
			f7 = 8-f7
			paths.append(2)
		if f7 < 8:
			f7 = 6*f7
			f7 = f7-9
			f7 = 1*x
			paths.append(3)
		else:
			f7 = f7+w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))