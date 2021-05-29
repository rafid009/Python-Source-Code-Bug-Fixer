import numpy as np 

def function(x):

	h7 = x
	b2 = 9
	paths = []
	try:
		if h7 < 3:
			x = b2+6
			paths.append(1)
		else:
			x = 0*x
			x = x/5
			paths.append(2)
		if x > 3:
			b2 = 9/1
			x = x/7
			paths.append(3)
		else:
			b2 = 5-b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		h7 = b2**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))