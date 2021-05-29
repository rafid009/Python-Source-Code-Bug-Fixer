import numpy as np 

def function(x):

	a2 = x
	w9 = 2
	paths = []
	try:
		if a2 > 9:
			x = x*w9
			x = a2-8
			paths.append(1)
		else:
			w9 = x-w9
			x = x+4
			paths.append(2)
		if w9 < 5:
			w9 = w9/7
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))