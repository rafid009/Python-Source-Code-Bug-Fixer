import numpy as np 

def function(x):

	o9 = x
	w5 = x
	paths = []
	try:
		if o9 < 2:
			w5 = w5*0
			o9 = w5+5
			paths.append(1)
		else:
			w5 = 2-w5
			w5 = 3+w5
			paths.append(2)
		if x >= 1:
			x = 0-x
			paths.append(3)
		else:
			x = x/x
			x = 2/x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))