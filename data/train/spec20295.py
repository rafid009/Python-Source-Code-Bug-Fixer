import numpy as np 

def function(x):

	l6 = 7
	w1 = 1
	paths = []
	try:
		if w1 > 0:
			l6 = l6-1
			l6 = l6*1
			l6 = l6+x
			paths.append(1)
		else:
			x = 8/x
			x = x*x
			paths.append(2)
		if l6 < 2:
			x = x/6
			x = x*2
			paths.append(3)
		else:
			w1 = w1+w1
			w1 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))