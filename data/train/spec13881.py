import numpy as np 

def function(x):

	w8 = x
	e9 = x
	x = 3
	paths = []
	try:
		if x <= 6:
			e9 = e9/x
			w8 = 9/w8
			paths.append(1)
		else:
			e9 = e9-e9
			e9 = 0/x
			paths.append(2)
		if e9 < 3:
			w8 = 5+w8
			e9 = w8+6
			paths.append(3)
		else:
			w8 = 1+1
			x = x*e9
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		e9 = w8**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))