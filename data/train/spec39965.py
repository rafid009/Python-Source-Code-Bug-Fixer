import numpy as np 

def function(x):

	w5 = 5
	f4 = x
	paths = []
	try:
		if x < 2:
			f4 = 5+3
			w5 = x-w5
			paths.append(1)
		else:
			f4 = 0/f4
			w5 = 0*8
			paths.append(2)
		if f4 > 2:
			w5 = w5/x
			paths.append(3)
		else:
			x = x-9
			w5 = 3*w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		f4 = w5**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))