import numpy as np 

def function(x):

	a8 = 7
	w1 = x
	paths = []
	try:
		if a8 <= 8:
			w1 = w1/4
			a8 = x+a8
			paths.append(1)
		else:
			x = 2+x
			x = 0+x
			a8 = 9/a8
			paths.append(2)
		if x > 9:
			w1 = a8+w1
			a8 = a8+1
			w1 = w1+w1
			paths.append(3)
		else:
			a8 = a8+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))