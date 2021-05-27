import numpy as np 

def function(x):

	w7 = 5
	e8 = x
	paths = []
	try:
		if x <= 5:
			w7 = 4*w7
			x = x/4
			paths.append(1)
		else:
			w7 = 8*3
			w7 = w7+5
			w7 = w7+x
			paths.append(2)
		if e8 < 8:
			x = 9+6
			w7 = x*e8
			paths.append(3)
		else:
			e8 = e8-7
			x = x*w7
			x = w7-8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))