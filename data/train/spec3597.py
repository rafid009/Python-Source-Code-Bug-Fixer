import numpy as np 

def function(x):

	a5 = x
	w6 = x
	paths = []
	try:
		if w6 >= 1:
			a5 = x-2
			w6 = w6*3
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if a5 < 0:
			x = x*x
			x = x+5
			paths.append(3)
		else:
			a5 = a5*8
			a5 = a5-8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		a5 = w6**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))