import numpy as np 

def function(x):

	b6 = x
	h2 = x
	paths = []
	try:
		if h2 >= 6:
			h2 = 3/3
			x = 1/x
			x = 1*x
			paths.append(1)
		else:
			b6 = 1+h2
			x = x+4
			x = b6+h2
			paths.append(2)
		if b6 <= 8:
			x = x/b6
			x = x*x
			h2 = h2+2
			paths.append(3)
		else:
			b6 = b6-3
			x = x-5
			h2 = 7+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))