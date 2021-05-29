import numpy as np 

def function(x):

	w2 = 0
	a9 = x
	paths = []
	try:
		if w2 < 2:
			a9 = 4/4
			paths.append(1)
		else:
			w2 = w2*x
			w2 = w2-6
			paths.append(2)
		if a9 <= 5:
			a9 = 7+7
			x = x+9
			paths.append(3)
		else:
			x = 7-a9
			x = x*w2
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))