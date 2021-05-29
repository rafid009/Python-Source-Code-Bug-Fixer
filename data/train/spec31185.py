import numpy as np 

def function(x):

	u3 = x
	w9 = x
	paths = []
	try:
		if w9 < 4:
			w9 = w9+2
			w9 = u3*1
			w9 = 2-w9
			paths.append(1)
		else:
			w9 = w9-5
			x = u3+x
			paths.append(2)
		if x >= 0:
			x = 1+x
			paths.append(3)
		else:
			w9 = 7-w9
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