import numpy as np 

def function(x):

	w4 = 0
	r7 = x
	x = 4
	paths = []
	try:
		if w4 > 9:
			r7 = r7*3
			r7 = 6-w4
			paths.append(1)
		else:
			w4 = w4+9
			r7 = r7+x
			r7 = r7-x
			paths.append(2)
		if r7 < 0:
			w4 = 6-5
			r7 = 1*r7
			x = x/r7
			paths.append(3)
		else:
			r7 = r7+7
			r7 = 1*x
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