import numpy as np 

def function(x):

	e8 = x
	f1 = x
	paths = []
	try:
		if f1 > 9:
			e8 = f1*7
			e8 = x-e8
			paths.append(1)
		else:
			f1 = f1+x
			f1 = 7*6
			paths.append(2)
		if x > 2:
			x = 5*x
			e8 = e8/1
			e8 = e8*e8
			paths.append(3)
		else:
			f1 = f1*e8
			e8 = e8-6
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