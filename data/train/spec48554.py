import numpy as np 

def function(x):

	r1 = x
	w9 = x
	paths = []
	try:
		if r1 >= 0:
			w9 = 2/x
			x = x*5
			paths.append(1)
		else:
			w9 = x+w9
			r1 = w9/r1
			r1 = 9/2
			paths.append(2)
		if r1 > 2:
			r1 = 7-r1
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		r1 = w9**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))