import numpy as np 

def function(x):

	l5 = 5
	w7 = x
	paths = []
	try:
		if l5 < 7:
			l5 = l5+8
			l5 = l5*6
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if l5 > 9:
			w7 = 2*0
			l5 = w7-l5
			l5 = l5+l5
			paths.append(3)
		else:
			w7 = w7/w7
			w7 = 8*l5
			w7 = 6+w7
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