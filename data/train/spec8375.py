import numpy as np 

def function(x):

	h1 = x
	w5 = 4
	paths = []
	try:
		if x >= 4:
			w5 = 8/w5
			w5 = 8*w5
			w5 = w5/6
			paths.append(1)
		else:
			h1 = h1-8
			x = x*1
			x = x*h1
			paths.append(2)
		if h1 > 7:
			x = x+3
			h1 = 4*2
			h1 = h1-x
			paths.append(3)
		else:
			h1 = h1+h1
			h1 = h1-2
			x = x*6
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		w5 = h1**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))