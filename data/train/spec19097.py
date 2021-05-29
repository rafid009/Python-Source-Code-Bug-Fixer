import numpy as np 

def function(x):

	g8 = x
	r7 = x
	paths = []
	try:
		if x >= 6:
			r7 = r7+1
			paths.append(1)
		else:
			r7 = g8/5
			paths.append(2)
		if r7 >= 9:
			x = x/7
			r7 = 1/7
			r7 = 9+x
			paths.append(3)
		else:
			r7 = 4/r7
			r7 = x*5
			x = x*6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		r7 = g8**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))