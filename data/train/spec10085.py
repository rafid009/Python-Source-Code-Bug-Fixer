import numpy as np 

def function(x):

	w2 = 7
	a4 = x
	x = 9
	paths = []
	try:
		if x < 3:
			a4 = 0-a4
			paths.append(1)
		else:
			a4 = a4/7
			x = a4-0
			x = 3/w2
			paths.append(2)
		if a4 <= 9:
			a4 = x*a4
			x = 8-w2
			paths.append(3)
		else:
			w2 = w2/a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		w2 = a4**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))