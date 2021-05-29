import numpy as np 

def function(x):

	f3 = 0
	w4 = x
	x = 0
	paths = []
	try:
		if w4 >= 9:
			x = x*f3
			x = x-6
			f3 = w4/x
			paths.append(1)
		else:
			w4 = 4*3
			paths.append(2)
		if w4 > 1:
			x = f3/w4
			x = 2*x
			paths.append(3)
		else:
			f3 = f3*8
			f3 = 8+f3
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))