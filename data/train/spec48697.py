import numpy as np 

def function(x):

	w6 = 9
	e1 = x
	paths = []
	try:
		if e1 >= 4:
			e1 = 8+w6
			e1 = e1+e1
			paths.append(1)
		else:
			w6 = w6/9
			x = x/3
			w6 = x*x
			paths.append(2)
		if e1 > 4:
			w6 = 2+3
			e1 = 8-e1
			paths.append(3)
		else:
			x = w6-6
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))