import numpy as np 

def function(x):

	w2 = 9
	a2 = x
	paths = []
	try:
		if w2 > 9:
			x = x+5
			paths.append(1)
		else:
			w2 = x*5
			x = 8+w2
			paths.append(2)
		if a2 >= 7:
			w2 = x/x
			w2 = w2-2
			paths.append(3)
		else:
			x = 5/5
			x = x/a2
			a2 = 3*a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))