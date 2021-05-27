import numpy as np 

def function(x):

	r0 = x
	w2 = 2
	paths = []
	try:
		if r0 <= 1:
			w2 = w2+w2
			r0 = r0/x
			paths.append(1)
		else:
			w2 = 3-w2
			r0 = 1/r0
			w2 = w2/2
			paths.append(2)
		if w2 <= 6:
			w2 = r0*2
			r0 = 6/r0
			r0 = 6-r0
			paths.append(3)
		else:
			r0 = 7*w2
			r0 = w2*4
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))