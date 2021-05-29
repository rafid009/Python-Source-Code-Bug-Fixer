import numpy as np 

def function(x):

	q7 = x
	w9 = x
	paths = []
	try:
		if x > 4:
			x = w9*7
			x = 2*x
			x = 8+1
			paths.append(1)
		else:
			q7 = q7*5
			paths.append(2)
		if q7 < 3:
			w9 = 2+w9
			q7 = 0+x
			w9 = w9/9
			paths.append(3)
		else:
			w9 = 0-7
			q7 = q7*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))