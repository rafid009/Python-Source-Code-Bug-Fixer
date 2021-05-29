import numpy as np 

def function(x):

	w3 = x
	b8 = 9
	paths = []
	try:
		if x > 5:
			w3 = w3-x
			paths.append(1)
		else:
			x = x+9
			x = x*3
			w3 = b8*8
			paths.append(2)
		if b8 < 9:
			b8 = b8*b8
			w3 = w3-0
			paths.append(3)
		else:
			b8 = b8/9
			w3 = 6+x
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