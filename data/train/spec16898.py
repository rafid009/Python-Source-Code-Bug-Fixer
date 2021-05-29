import numpy as np 

def function(x):

	w2 = 1
	w3 = 9
	paths = []
	try:
		if w3 < 4:
			w2 = w2+4
			paths.append(1)
		else:
			w3 = w3-7
			x = 1/x
			w3 = 3/w3
			paths.append(2)
		if w2 > 0:
			w2 = x*4
			w2 = x+1
			w2 = w2-9
			paths.append(3)
		else:
			x = x-5
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))