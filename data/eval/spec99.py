import numpy as np 

def function(x):

	r4 = 1
	h7 = x
	paths = []
	try:
		if h7 < 0:
			h7 = 1+8
			x = h7+r4
			r4 = 7-r4
			paths.append(1)
		else:
			x = x/x
			r4 = 2+7
			paths.append(2)
		if r4 >= 7:
			r4 = r4*4
			r4 = h7*2
			paths.append(3)
		else:
			h7 = 4-9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		r4 = h7**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))