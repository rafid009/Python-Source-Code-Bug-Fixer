import numpy as np 

def function(x):

	w7 = 4
	l6 = x
	paths = []
	try:
		if l6 < 5:
			l6 = 0/l6
			paths.append(1)
		else:
			l6 = x/1
			l6 = l6*5
			x = 4*w7
			paths.append(2)
		if x <= 6:
			w7 = w7-l6
			paths.append(3)
		else:
			w7 = x*0
			x = w7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))