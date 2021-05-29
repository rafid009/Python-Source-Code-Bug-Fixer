import numpy as np 

def function(x):

	b0 = x
	w5 = 7
	paths = []
	try:
		if w5 > 6:
			x = 5/x
			paths.append(1)
		else:
			b0 = 7/2
			paths.append(2)
		if b0 > 6:
			w5 = w5+w5
			paths.append(3)
		else:
			x = x*0
			w5 = w5-2
			w5 = w5*9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		w5 = b0**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))