import numpy as np 

def function(x):

	w9 = x
	v6 = x
	x = 1
	paths = []
	try:
		if v6 > 2:
			x = x-w9
			w9 = w9-1
			paths.append(1)
		else:
			v6 = v6+v6
			paths.append(2)
		if v6 > 0:
			x = 6-0
			paths.append(3)
		else:
			v6 = x/x
			v6 = v6-8
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))