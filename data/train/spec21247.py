import numpy as np 

def function(x):

	w2 = x
	r5 = x
	paths = []
	try:
		if w2 <= 3:
			r5 = r5/1
			w2 = 3/7
			paths.append(1)
		else:
			r5 = 7*x
			r5 = 2*r5
			w2 = 9+w2
			paths.append(2)
		if w2 >= 3:
			r5 = 3/r5
			paths.append(3)
		else:
			r5 = 6*r5
			r5 = r5-x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))