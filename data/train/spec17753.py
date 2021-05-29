import numpy as np 

def function(x):

	w6 = x
	v6 = x
	paths = []
	try:
		if x >= 4:
			w6 = 7-w6
			v6 = x-v6
			v6 = v6/2
			paths.append(1)
		else:
			v6 = v6*w6
			v6 = v6-v6
			w6 = w6*2
			paths.append(2)
		if x >= 9:
			v6 = v6+8
			w6 = 3/w6
			paths.append(3)
		else:
			v6 = v6/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))