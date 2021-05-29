import numpy as np 

def function(x):

	s2 = x
	h0 = x
	paths = []
	try:
		if s2 < 2:
			s2 = 4+s2
			x = x/8
			h0 = s2*x
			paths.append(1)
		else:
			h0 = 5+h0
			s2 = 4-0
			paths.append(2)
		if h0 <= 9:
			h0 = h0+h0
			x = x+h0
			x = 6+x
			paths.append(3)
		else:
			h0 = 0+5
			s2 = x/s2
			s2 = s2+5
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))