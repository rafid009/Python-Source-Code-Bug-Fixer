import numpy as np 

def function(x):

	w7 = x
	u3 = x
	paths = []
	try:
		if x >= 8:
			x = 4-9
			paths.append(1)
		else:
			w7 = w7+5
			x = 1+w7
			paths.append(2)
		if x <= 3:
			w7 = w7-2
			u3 = u3+w7
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))