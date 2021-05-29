import numpy as np 

def function(x):

	w3 = x
	i7 = 3
	x = x
	paths = []
	try:
		if w3 < 6:
			w3 = 1+w3
			i7 = i7*i7
			paths.append(1)
		else:
			i7 = i7*5
			paths.append(2)
		if w3 >= 7:
			i7 = 4-0
			i7 = i7*2
			w3 = w3+i7
			paths.append(3)
		else:
			w3 = 9+w3
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))