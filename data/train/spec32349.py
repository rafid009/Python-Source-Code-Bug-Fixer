import numpy as np 

def function(x):

	f1 = 4
	d7 = 5
	paths = []
	try:
		if f1 <= 5:
			f1 = f1-x
			paths.append(1)
		else:
			f1 = 8*f1
			d7 = d7-5
			paths.append(2)
		if d7 > 4:
			d7 = d7*x
			f1 = 0+8
			f1 = d7-1
			paths.append(3)
		else:
			f1 = 2/f1
			d7 = d7-9
			x = 0*5
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		f1 = d7**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))