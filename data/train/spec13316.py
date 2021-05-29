import numpy as np 

def function(x):

	l5 = x
	h0 = x
	x = 9
	paths = []
	try:
		if h0 >= 2:
			h0 = 4+h0
			paths.append(1)
		else:
			l5 = 3*0
			h0 = h0*3
			x = x*3
			paths.append(2)
		if l5 <= 0:
			l5 = x+l5
			h0 = h0*7
			h0 = 0/7
			paths.append(3)
		else:
			l5 = l5-h0
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))