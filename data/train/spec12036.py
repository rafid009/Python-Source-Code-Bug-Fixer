import numpy as np 

def function(x):

	s5 = x
	h4 = 7
	x = 8
	paths = []
	try:
		if x <= 8:
			s5 = 0*3
			x = x+s5
			x = x/2
			paths.append(1)
		else:
			h4 = x-h4
			s5 = s5+2
			paths.append(2)
		if h4 < 9:
			h4 = 2-9
			h4 = h4*2
			paths.append(3)
		else:
			s5 = 5/8
			x = 3-x
			h4 = 8/9
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))