import numpy as np 

def function(x):

	w5 = 7
	e1 = x
	paths = []
	try:
		if w5 < 4:
			x = x+x
			paths.append(1)
		else:
			w5 = x*w5
			x = x/2
			e1 = x+2
			paths.append(2)
		if x > 9:
			x = x/x
			paths.append(3)
		else:
			e1 = e1+x
			e1 = 9*4
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		e1 = w5**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))