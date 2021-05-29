import numpy as np 

def function(x):

	b0 = x
	r4 = 0
	paths = []
	try:
		if x < 8:
			x = x/b0
			x = 1+x
			r4 = r4+r4
			paths.append(1)
		else:
			r4 = 5+r4
			r4 = r4+5
			b0 = 3/x
			paths.append(2)
		if r4 >= 9:
			x = x-b0
			paths.append(3)
		else:
			x = 3+3
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		r4 = b0**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))