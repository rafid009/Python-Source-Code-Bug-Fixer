import numpy as np 

def function(x):

	a1 = 9
	w2 = 7
	paths = []
	try:
		if a1 < 5:
			a1 = a1+6
			paths.append(1)
		else:
			a1 = a1-7
			a1 = a1-8
			paths.append(2)
		if x >= 1:
			w2 = w2-5
			w2 = w2-3
			a1 = a1/2
			paths.append(3)
		else:
			w2 = w2*w2
			x = w2-6
			w2 = w2*3
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))