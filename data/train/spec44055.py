import numpy as np 

def function(x):

	j5 = 5
	w3 = x
	x = x
	paths = []
	try:
		if w3 >= 9:
			x = j5/x
			x = j5+w3
			x = x-2
			paths.append(1)
		else:
			w3 = w3/1
			j5 = 5-x
			w3 = j5*w3
			paths.append(2)
		if w3 > 5:
			j5 = 9-w3
			x = x*5
			paths.append(3)
		else:
			w3 = w3/j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		w3 = j5**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))