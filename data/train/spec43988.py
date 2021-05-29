import numpy as np 

def function(x):

	e0 = x
	w2 = 3
	paths = []
	try:
		if e0 > 3:
			e0 = w2*4
			paths.append(1)
		else:
			e0 = e0/6
			e0 = e0*e0
			w2 = w2-6
			paths.append(2)
		if e0 <= 5:
			e0 = e0-x
			x = x/3
			paths.append(3)
		else:
			w2 = 9/1
			x = x-x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		w2 = e0**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))