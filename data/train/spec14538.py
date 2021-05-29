import numpy as np 

def function(x):

	b9 = 5
	h0 = x
	paths = []
	try:
		if h0 > 1:
			x = h0/9
			paths.append(1)
		else:
			h0 = 4+h0
			x = x*8
			x = x/2
			paths.append(2)
		if h0 < 5:
			b9 = b9-x
			x = x+b9
			b9 = 3/b9
			paths.append(3)
		else:
			b9 = b9-5
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		b9 = h0**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))