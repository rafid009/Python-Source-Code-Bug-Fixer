import numpy as np 

def function(x):

	w7 = 3
	l5 = 9
	x = x
	paths = []
	try:
		if l5 >= 2:
			l5 = w7*l5
			x = x/1
			l5 = x-l5
			paths.append(1)
		else:
			l5 = l5+9
			w7 = l5+w7
			l5 = x+l5
			paths.append(2)
		if w7 < 1:
			w7 = 6*w7
			x = x*7
			paths.append(3)
		else:
			w7 = 8*w7
			x = 5*l5
			l5 = l5/w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))