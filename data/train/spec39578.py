import numpy as np 

def function(x):

	w0 = x
	v6 = 4
	paths = []
	try:
		if v6 > 7:
			x = w0*w0
			paths.append(1)
		else:
			v6 = v6-w0
			x = x-4
			v6 = 0*v6
			paths.append(2)
		if x >= 7:
			v6 = v6-4
			w0 = w0/7
			paths.append(3)
		else:
			x = 5+x
			w0 = 6/2
			v6 = v6*2
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		w0 = v6**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))