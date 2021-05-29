import numpy as np 

def function(x):

	u3 = x
	h3 = 4
	paths = []
	try:
		if u3 <= 1:
			x = 1*x
			h3 = 8*h3
			u3 = u3-6
			paths.append(1)
		else:
			x = u3+u3
			paths.append(2)
		if u3 > 5:
			h3 = h3-4
			paths.append(3)
		else:
			u3 = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))