import numpy as np 

def function(x):

	w1 = 6
	h1 = x
	paths = []
	try:
		if w1 >= 3:
			w1 = 1+w1
			paths.append(1)
		else:
			x = w1/9
			h1 = 6-h1
			x = x*8
			paths.append(2)
		if w1 <= 3:
			x = h1+0
			w1 = 6+8
			paths.append(3)
		else:
			w1 = 9+x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))