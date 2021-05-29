import numpy as np 

def function(x):

	f1 = x
	d1 = x
	x = x
	paths = []
	try:
		if f1 > 8:
			d1 = 3+9
			paths.append(1)
		else:
			f1 = f1/1
			x = x/x
			paths.append(2)
		if x <= 9:
			f1 = f1*6
			d1 = d1-6
			x = x-4
			paths.append(3)
		else:
			f1 = 5*4
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