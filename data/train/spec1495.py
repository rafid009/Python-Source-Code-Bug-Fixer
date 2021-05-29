import numpy as np 

def function(x):

	k1 = x
	w6 = 5
	paths = []
	try:
		if x <= 1:
			x = x-2
			w6 = 9+w6
			paths.append(1)
		else:
			k1 = k1+x
			paths.append(2)
		if x <= 7:
			w6 = k1-w6
			w6 = w6-w6
			paths.append(3)
		else:
			w6 = w6-w6
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		w6 = k1**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))