import numpy as np 

def function(x):

	h8 = x
	r8 = x
	paths = []
	try:
		if x >= 7:
			x = x+x
			x = 6+9
			paths.append(1)
		else:
			x = r8/x
			x = x-8
			h8 = 5+h8
			paths.append(2)
		if h8 < 9:
			x = x/5
			x = x-5
			paths.append(3)
		else:
			r8 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))