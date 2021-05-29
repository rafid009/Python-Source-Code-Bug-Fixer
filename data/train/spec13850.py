import numpy as np 

def function(x):

	q5 = 7
	w6 = 7
	paths = []
	try:
		if q5 > 3:
			w6 = q5/9
			w6 = 7-w6
			w6 = w6-7
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if x <= 4:
			x = x-3
			q5 = q5*8
			w6 = x+w6
			paths.append(3)
		else:
			x = 9+x
			q5 = q5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))