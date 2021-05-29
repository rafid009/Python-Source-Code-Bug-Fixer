import numpy as np 

def function(x):

	w0 = x
	u5 = 2
	x = x
	paths = []
	try:
		if u5 < 3:
			w0 = 1*w0
			w0 = 2/w0
			u5 = u5-0
			paths.append(1)
		else:
			w0 = x*w0
			u5 = 0+0
			x = 4-5
			paths.append(2)
		if x > 5:
			w0 = w0*9
			paths.append(3)
		else:
			x = x/5
			u5 = 0/u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))