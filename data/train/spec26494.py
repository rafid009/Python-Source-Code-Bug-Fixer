import numpy as np 

def function(x):

	j7 = x
	w6 = x
	paths = []
	try:
		if j7 <= 7:
			w6 = 1/4
			x = x/x
			w6 = w6*w6
			paths.append(1)
		else:
			x = w6-x
			w6 = w6/9
			paths.append(2)
		if w6 > 6:
			x = x/4
			j7 = 8*x
			paths.append(3)
		else:
			x = j7+3
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))