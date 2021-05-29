import numpy as np 

def function(x):

	h0 = x
	l8 = x
	paths = []
	try:
		if l8 <= 1:
			h0 = 1+h0
			x = h0+x
			l8 = l8+x
			paths.append(1)
		else:
			l8 = h0+7
			paths.append(2)
		if x <= 7:
			h0 = h0/h0
			h0 = h0-2
			x = 6+5
			paths.append(3)
		else:
			h0 = h0*h0
			x = x*x
			l8 = l8/6
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		l8 = h0**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))