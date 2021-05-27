import numpy as np 

def function(x):

	e0 = x
	w7 = 0
	paths = []
	try:
		if e0 <= 4:
			w7 = w7-2
			e0 = 7+e0
			paths.append(1)
		else:
			w7 = e0+6
			paths.append(2)
		if x < 7:
			x = e0*8
			paths.append(3)
		else:
			x = x/5
			e0 = 4-0
			w7 = w7-w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))