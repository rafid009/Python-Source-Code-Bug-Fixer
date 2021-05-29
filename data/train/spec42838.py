import numpy as np 

def function(x):

	f1 = x
	w0 = 7
	paths = []
	try:
		if w0 > 0:
			f1 = f1*1
			x = x/3
			paths.append(1)
		else:
			w0 = w0+1
			f1 = f1+5
			paths.append(2)
		if f1 > 2:
			f1 = f1+f1
			paths.append(3)
		else:
			f1 = 2-6
			x = 5/x
			w0 = w0/4
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