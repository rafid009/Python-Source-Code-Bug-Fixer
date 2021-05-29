import numpy as np 

def function(x):

	a2 = 9
	w6 = 1
	x = 7
	paths = []
	try:
		if w6 >= 5:
			a2 = 5-8
			w6 = 5*w6
			paths.append(1)
		else:
			a2 = 2-a2
			w6 = 8-3
			w6 = a2-9
			paths.append(2)
		if x > 3:
			w6 = 6/w6
			a2 = a2*7
			paths.append(3)
		else:
			w6 = w6*w6
			w6 = w6+9
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))