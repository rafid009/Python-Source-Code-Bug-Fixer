import numpy as np 

def function(x):

	w9 = x
	a7 = x
	paths = []
	try:
		if a7 > 8:
			x = 1*x
			w9 = 9*w9
			x = x-x
			paths.append(1)
		else:
			w9 = w9/2
			paths.append(2)
		if a7 > 9:
			a7 = x*2
			w9 = w9*w9
			paths.append(3)
		else:
			x = 7+2
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))