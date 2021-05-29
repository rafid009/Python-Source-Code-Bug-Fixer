import numpy as np 

def function(x):

	i9 = 1
	w9 = x
	paths = []
	try:
		if w9 > 8:
			x = 7-1
			i9 = i9+3
			paths.append(1)
		else:
			i9 = 4-i9
			w9 = x-5
			i9 = i9*i9
			paths.append(2)
		if x <= 7:
			x = i9+x
			paths.append(3)
		else:
			x = x-w9
			i9 = w9-i9
			w9 = x/5
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