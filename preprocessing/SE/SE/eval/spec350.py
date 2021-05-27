import numpy as np 

def function(x):

	w6 = x
	q7 = x
	paths = []
	try:
		if q7 < 4:
			q7 = x-q7
			paths.append(1)
		else:
			x = x*x
			w6 = 8+2
			paths.append(2)
		if q7 >= 2:
			w6 = q7+3
			q7 = q7-5
			w6 = w6/q7
			paths.append(3)
		else:
			w6 = w6+x
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))