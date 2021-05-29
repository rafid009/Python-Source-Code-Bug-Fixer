import numpy as np 

def function(x):

	g5 = x
	u3 = x
	paths = []
	try:
		if u3 < 8:
			u3 = g5*u3
			u3 = u3/1
			u3 = g5+u3
			paths.append(1)
		else:
			u3 = 9/2
			paths.append(2)
		if x <= 1:
			x = 2/x
			u3 = g5*x
			g5 = 2*8
			paths.append(3)
		else:
			x = x-2
			g5 = 2-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))