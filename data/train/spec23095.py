import numpy as np 

def function(x):

	n0 = x
	f1 = 7
	x = x
	paths = []
	try:
		if x <= 4:
			x = x/7
			f1 = n0/f1
			f1 = 7/5
			paths.append(1)
		else:
			f1 = f1*x
			n0 = n0*5
			n0 = 9+5
			paths.append(2)
		if n0 <= 7:
			n0 = 5+0
			n0 = 4/1
			paths.append(3)
		else:
			n0 = 8*n0
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