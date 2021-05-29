import numpy as np 

def function(x):

	w7 = x
	w9 = 3
	x = x
	paths = []
	try:
		if w9 >= 8:
			w7 = 6/w7
			w7 = w7+w9
			paths.append(1)
		else:
			w9 = w9+x
			w7 = 7+w7
			paths.append(2)
		if w7 <= 6:
			w7 = 4*w7
			paths.append(3)
		else:
			w9 = x+4
			w7 = w7*3
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w7 = w9**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))