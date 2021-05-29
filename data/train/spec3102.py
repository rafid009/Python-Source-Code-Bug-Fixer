import numpy as np 

def function(x):

	w8 = 3
	o5 = x
	paths = []
	try:
		if w8 > 5:
			w8 = 7*w8
			w8 = w8+1
			o5 = w8/9
			paths.append(1)
		else:
			w8 = 0-4
			paths.append(2)
		if o5 < 1:
			x = 6/x
			x = 0+x
			x = 4*x
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))