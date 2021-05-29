import numpy as np 

def function(x):

	b8 = 9
	h0 = 2
	paths = []
	try:
		if x > 8:
			x = x/9
			x = 3+x
			h0 = h0+h0
			paths.append(1)
		else:
			b8 = b8-8
			paths.append(2)
		if b8 >= 3:
			x = x/5
			x = x+9
			paths.append(3)
		else:
			b8 = 2+b8
			h0 = 7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))