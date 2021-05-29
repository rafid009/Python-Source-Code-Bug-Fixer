import numpy as np 

def function(x):

	b5 = x
	w2 = 2
	paths = []
	try:
		if b5 >= 1:
			x = x*6
			b5 = 5+6
			b5 = b5+1
			paths.append(1)
		else:
			x = x/x
			x = 8/x
			b5 = b5*4
			paths.append(2)
		if w2 < 7:
			w2 = w2+2
			paths.append(3)
		else:
			w2 = 7+8
			x = 2/x
			b5 = b5*x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		w2 = b5**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))