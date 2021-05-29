import numpy as np 

def function(x):

	w9 = x
	e1 = 7
	paths = []
	try:
		if x < 6:
			e1 = e1*w9
			paths.append(1)
		else:
			w9 = e1*2
			x = x-x
			e1 = x/e1
			paths.append(2)
		if w9 < 5:
			x = e1-e1
			e1 = 4*e1
			w9 = w9/4
			paths.append(3)
		else:
			e1 = x+3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))