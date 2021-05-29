import numpy as np 

def function(x):

	r6 = x
	w2 = 8
	paths = []
	try:
		if w2 < 7:
			r6 = x/r6
			w2 = x/8
			paths.append(1)
		else:
			x = x+6
			r6 = w2/r6
			w2 = 3*w2
			paths.append(2)
		if w2 <= 7:
			w2 = 7/6
			w2 = 2*x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))