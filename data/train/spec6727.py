import numpy as np 

def function(x):

	h6 = 6
	n3 = 2
	paths = []
	try:
		if n3 > 2:
			h6 = 2+h6
			n3 = 5-n3
			paths.append(1)
		else:
			x = h6*x
			n3 = 9+4
			x = 9+x
			paths.append(2)
		if h6 > 7:
			n3 = 7-h6
			x = x*1
			x = x*x
			paths.append(3)
		else:
			h6 = n3*4
			n3 = 6-7
			x = n3*2
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))