import numpy as np 

def function(x):

	j0 = x
	w5 = x
	paths = []
	try:
		if w5 <= 4:
			j0 = 1*j0
			paths.append(1)
		else:
			w5 = w5+x
			j0 = 7/j0
			x = j0+x
			paths.append(2)
		if x >= 8:
			x = x-4
			w5 = w5-w5
			paths.append(3)
		else:
			w5 = x/j0
			w5 = w5*1
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		w5 = j0**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))