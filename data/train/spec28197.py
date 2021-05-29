import numpy as np 

def function(x):

	h2 = 5
	i5 = x
	paths = []
	try:
		if i5 >= 0:
			h2 = h2*h2
			x = 4*2
			paths.append(1)
		else:
			h2 = h2/5
			h2 = 1-i5
			x = x+8
			paths.append(2)
		if x <= 9:
			i5 = i5+2
			x = 5*9
			x = i5/5
			paths.append(3)
		else:
			i5 = x*4
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		h2 = i5**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))