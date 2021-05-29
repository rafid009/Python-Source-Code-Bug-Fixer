import numpy as np 

def function(x):

	w9 = 3
	r7 = x
	paths = []
	try:
		if r7 < 8:
			w9 = r7/w9
			r7 = 0-r7
			paths.append(1)
		else:
			x = 6/x
			r7 = 5*0
			paths.append(2)
		if w9 < 9:
			x = x*3
			paths.append(3)
		else:
			x = r7-r7
			r7 = 5/r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))