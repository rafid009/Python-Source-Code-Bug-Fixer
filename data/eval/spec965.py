import numpy as np 

def function(x):

	w9 = 6
	x9 = x
	paths = []
	try:
		if x < 9:
			x9 = x+x9
			x = x*0
			paths.append(1)
		else:
			w9 = w9-6
			paths.append(2)
		if w9 < 6:
			x9 = x9/x9
			paths.append(3)
		else:
			x = 2-7
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))