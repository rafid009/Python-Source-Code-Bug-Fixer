import numpy as np 

def function(x):

	v7 = x
	w7 = 3
	x = x
	paths = []
	try:
		if w7 <= 2:
			v7 = v7-3
			w7 = 5/x
			paths.append(1)
		else:
			x = x-5
			v7 = v7+5
			x = x*3
			paths.append(2)
		if x >= 1:
			w7 = w7*0
			paths.append(3)
		else:
			v7 = 3+x
			w7 = w7-1
			w7 = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))