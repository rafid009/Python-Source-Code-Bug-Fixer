import numpy as np 

def function(x):

	e5 = x
	w6 = 3
	paths = []
	try:
		if e5 < 2:
			x = x+9
			w6 = w6*w6
			e5 = 5/x
			paths.append(1)
		else:
			w6 = 1+w6
			x = 7-3
			e5 = 5/e5
			paths.append(2)
		if x <= 7:
			x = 6+x
			paths.append(3)
		else:
			w6 = w6*w6
			w6 = 5-e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		w6 = e5**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))