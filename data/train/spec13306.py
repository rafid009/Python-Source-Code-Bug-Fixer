import numpy as np 

def function(x):

	w2 = x
	h6 = 2
	x = 8
	paths = []
	try:
		if x > 7:
			x = x*7
			h6 = x*h6
			x = x*w2
			paths.append(1)
		else:
			x = x/w2
			x = x*8
			w2 = x/6
			paths.append(2)
		if x > 4:
			h6 = h6+h6
			w2 = x+0
			paths.append(3)
		else:
			h6 = 1*1
			w2 = w2+5
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