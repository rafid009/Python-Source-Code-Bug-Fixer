import numpy as np 

def function(x):

	v3 = 3
	w3 = 9
	paths = []
	try:
		if x > 8:
			v3 = x/v3
			w3 = 3-2
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if w3 <= 7:
			x = 0*x
			w3 = 5*9
			x = 3*w3
			paths.append(3)
		else:
			w3 = v3-7
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))