import numpy as np 

def function(x):

	f5 = 4
	h7 = x
	paths = []
	try:
		if x <= 7:
			x = 5/x
			x = x*0
			paths.append(1)
		else:
			x = 8-h7
			paths.append(2)
		if h7 >= 2:
			x = x/2
			x = x*5
			f5 = 6+h7
			paths.append(3)
		else:
			x = x-9
			h7 = 6-f5
			x = x/h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))