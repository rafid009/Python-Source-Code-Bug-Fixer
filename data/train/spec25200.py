import numpy as np 

def function(x):

	w2 = 5
	j7 = x
	paths = []
	try:
		if w2 < 7:
			j7 = j7+3
			x = 1-7
			w2 = 8*w2
			paths.append(1)
		else:
			j7 = w2/j7
			paths.append(2)
		if w2 >= 1:
			j7 = j7/w2
			j7 = j7-5
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		w2 = j7**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))