import numpy as np 

def function(x):

	a4 = 1
	w1 = 6
	paths = []
	try:
		if a4 >= 4:
			a4 = 5/x
			w1 = a4+a4
			a4 = a4/w1
			paths.append(1)
		else:
			x = x+w1
			x = x+5
			paths.append(2)
		if x <= 9:
			a4 = 0-a4
			w1 = w1-7
			a4 = a4-3
			paths.append(3)
		else:
			a4 = 9*5
			a4 = a4-w1
			x = x+6
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		a4 = w1**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))