import numpy as np 

def function(x):

	w6 = x
	u3 = 5
	paths = []
	try:
		if w6 > 7:
			w6 = u3*w6
			x = 6/x
			paths.append(1)
		else:
			x = 1/u3
			w6 = 5/u3
			x = x/8
			paths.append(2)
		if w6 <= 0:
			u3 = u3-u3
			w6 = 4-w6
			w6 = w6*x
			paths.append(3)
		else:
			x = x+w6
			w6 = w6-4
			w6 = 1-x
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