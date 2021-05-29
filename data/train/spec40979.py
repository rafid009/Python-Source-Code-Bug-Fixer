import numpy as np 

def function(x):

	r4 = 8
	w2 = 9
	paths = []
	try:
		if r4 < 1:
			r4 = r4*9
			x = x*x
			paths.append(1)
		else:
			r4 = 5*0
			paths.append(2)
		if x >= 4:
			r4 = 0/8
			paths.append(3)
		else:
			w2 = 6-w2
			r4 = 2/x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))