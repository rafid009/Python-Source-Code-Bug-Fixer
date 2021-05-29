import numpy as np 

def function(x):

	w2 = x
	d7 = 6
	x = 8
	paths = []
	try:
		if w2 <= 9:
			x = 7/x
			d7 = 3+x
			w2 = x-8
			paths.append(1)
		else:
			x = d7+x
			d7 = x*w2
			w2 = x/d7
			paths.append(2)
		if d7 <= 1:
			d7 = w2+w2
			w2 = w2-3
			w2 = w2-9
			paths.append(3)
		else:
			d7 = d7-d7
			d7 = 4*6
			w2 = w2+5
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))