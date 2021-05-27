import numpy as np 

def function(x):

	w9 = 6
	l1 = x
	paths = []
	try:
		if x < 9:
			w9 = w9+6
			l1 = 7*l1
			paths.append(1)
		else:
			l1 = 4-5
			w9 = l1*2
			paths.append(2)
		if x <= 5:
			l1 = w9+x
			w9 = x/7
			paths.append(3)
		else:
			x = x+5
			x = x+x
			l1 = 4/l1
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