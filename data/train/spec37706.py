import numpy as np 

def function(x):

	w9 = 0
	b6 = x
	paths = []
	try:
		if x > 6:
			w9 = x/x
			b6 = 9-0
			paths.append(1)
		else:
			w9 = w9+x
			b6 = b6/8
			b6 = b6/4
			paths.append(2)
		if b6 <= 4:
			x = 3-x
			w9 = 6+w9
			paths.append(3)
		else:
			x = x*x
			x = b6/3
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))