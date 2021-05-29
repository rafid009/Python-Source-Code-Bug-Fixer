import numpy as np 

def function(x):

	v6 = 2
	w7 = x
	x = x
	paths = []
	try:
		if v6 < 2:
			v6 = 3-v6
			x = w7-4
			paths.append(1)
		else:
			x = w7+5
			paths.append(2)
		if x > 9:
			x = x+7
			w7 = w7/v6
			v6 = v6/1
			paths.append(3)
		else:
			x = w7/v6
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		v6 = w7**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))