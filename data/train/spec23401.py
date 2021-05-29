import numpy as np 

def function(x):

	r5 = 0
	w5 = x
	paths = []
	try:
		if x >= 2:
			w5 = r5-w5
			paths.append(1)
		else:
			x = 1+9
			r5 = r5+9
			x = 0-r5
			paths.append(2)
		if x >= 0:
			x = x*2
			r5 = 9+r5
			paths.append(3)
		else:
			x = 7*4
			r5 = w5+0
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))