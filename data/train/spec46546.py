import numpy as np 

def function(x):

	h2 = x
	r7 = 1
	paths = []
	try:
		if r7 >= 6:
			h2 = h2/h2
			x = x*3
			h2 = h2/h2
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if r7 <= 1:
			h2 = 9*h2
			h2 = h2*9
			r7 = h2-2
			paths.append(3)
		else:
			r7 = r7-r7
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))