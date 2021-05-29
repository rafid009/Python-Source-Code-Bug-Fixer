import numpy as np 

def function(x):

	v8 = 3
	w6 = x
	paths = []
	try:
		if v8 < 8:
			w6 = 9/2
			w6 = w6-w6
			paths.append(1)
		else:
			v8 = 1-0
			v8 = v8*2
			paths.append(2)
		if x >= 8:
			v8 = v8+v8
			x = x+6
			paths.append(3)
		else:
			w6 = w6*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))