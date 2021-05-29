import numpy as np 

def function(x):

	s9 = x
	h0 = 1
	paths = []
	try:
		if x > 0:
			x = s9+h0
			h0 = h0+9
			s9 = 6+s9
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x > 2:
			s9 = h0/h0
			paths.append(3)
		else:
			h0 = h0+7
			x = x+9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))