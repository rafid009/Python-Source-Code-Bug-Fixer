import numpy as np 

def function(x):

	w0 = x
	v8 = 3
	paths = []
	try:
		if v8 > 3:
			x = x*2
			v8 = v8-9
			paths.append(1)
		else:
			v8 = v8-w0
			w0 = 5+w0
			paths.append(2)
		if v8 < 4:
			x = 6/3
			x = x/v8
			paths.append(3)
		else:
			x = 9/x
			v8 = w0/x
			v8 = v8+1
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))