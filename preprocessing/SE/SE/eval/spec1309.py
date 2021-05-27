import numpy as np 

def function(x):

	e6 = x
	h0 = x
	paths = []
	try:
		if e6 < 7:
			x = 4*7
			x = h0*x
			paths.append(1)
		else:
			x = x+x
			x = x-2
			paths.append(2)
		if x > 4:
			h0 = x*h0
			paths.append(3)
		else:
			e6 = e6+8
			h0 = h0/x
			x = x*1
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))