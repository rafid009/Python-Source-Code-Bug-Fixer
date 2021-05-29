import numpy as np 

def function(x):

	n2 = x
	h7 = x
	paths = []
	try:
		if h7 < 3:
			h7 = h7+8
			x = x-7
			x = 5-4
			paths.append(1)
		else:
			n2 = n2+1
			n2 = n2*4
			x = x/h7
			paths.append(2)
		if n2 >= 2:
			x = x-n2
			paths.append(3)
		else:
			n2 = 5-n2
			n2 = 4+5
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		n2 = h7**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))