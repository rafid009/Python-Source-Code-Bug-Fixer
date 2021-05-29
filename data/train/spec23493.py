import numpy as np 

def function(x):

	w2 = 6
	r4 = 5
	paths = []
	try:
		if x >= 0:
			w2 = 8+x
			w2 = w2/x
			r4 = r4+r4
			paths.append(1)
		else:
			w2 = w2-2
			r4 = 6*2
			x = 2/x
			paths.append(2)
		if w2 <= 8:
			r4 = 6*3
			x = x/6
			paths.append(3)
		else:
			x = 7+x
			x = x*2
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))