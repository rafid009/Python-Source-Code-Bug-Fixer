import numpy as np 

def function(x):

	j7 = x
	w4 = x
	x = x
	paths = []
	try:
		if w4 > 4:
			x = 2+x
			paths.append(1)
		else:
			w4 = w4*2
			j7 = w4+j7
			paths.append(2)
		if w4 > 6:
			j7 = x-j7
			paths.append(3)
		else:
			j7 = j7/j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))