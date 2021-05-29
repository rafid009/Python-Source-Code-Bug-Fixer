import numpy as np 

def function(x):

	o0 = x
	u3 = x
	paths = []
	try:
		if o0 <= 2:
			o0 = o0+6
			u3 = 0+1
			paths.append(1)
		else:
			u3 = 8*u3
			u3 = u3-7
			u3 = 9*3
			paths.append(2)
		if u3 > 1:
			x = x*3
			paths.append(3)
		else:
			u3 = 3-7
			x = 6-7
			u3 = 1+u3
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