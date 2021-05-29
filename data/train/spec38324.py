import numpy as np 

def function(x):

	o8 = x
	f1 = 9
	paths = []
	try:
		if x > 7:
			x = x-7
			paths.append(1)
		else:
			x = o8-8
			paths.append(2)
		if x <= 6:
			x = x*3
			o8 = f1+4
			f1 = 2-x
			paths.append(3)
		else:
			o8 = 4/7
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))