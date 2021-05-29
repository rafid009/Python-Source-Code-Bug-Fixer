import numpy as np 

def function(x):

	d7 = x
	f1 = 5
	paths = []
	try:
		if f1 < 8:
			d7 = 1/d7
			paths.append(1)
		else:
			x = 8+7
			f1 = f1*7
			f1 = d7/5
			paths.append(2)
		if d7 > 6:
			d7 = f1/d7
			paths.append(3)
		else:
			f1 = f1/1
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