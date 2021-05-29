import numpy as np 

def function(x):

	v3 = x
	w7 = x
	x = 5
	paths = []
	try:
		if x <= 2:
			x = x/w7
			w7 = 3-w7
			paths.append(1)
		else:
			v3 = v3/2
			paths.append(2)
		if v3 <= 5:
			x = w7/4
			v3 = 4*v3
			paths.append(3)
		else:
			w7 = 9+w7
			v3 = 5+v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))