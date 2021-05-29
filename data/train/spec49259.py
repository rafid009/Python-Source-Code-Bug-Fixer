import numpy as np 

def function(x):

	u2 = 7
	w9 = x
	paths = []
	try:
		if u2 <= 6:
			u2 = w9+u2
			paths.append(1)
		else:
			u2 = u2-5
			x = x-7
			paths.append(2)
		if x > 8:
			x = 4+x
			u2 = 8*u2
			u2 = 0*u2
			paths.append(3)
		else:
			x = x*4
			w9 = w9-9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))