import numpy as np 

def function(x):

	r4 = x
	w2 = x
	x = 7
	paths = []
	try:
		if w2 < 6:
			r4 = x+2
			w2 = x-w2
			paths.append(1)
		else:
			w2 = w2-8
			paths.append(2)
		if w2 <= 4:
			w2 = 5/w2
			paths.append(3)
		else:
			r4 = 5/9
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		r4 = w2**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))