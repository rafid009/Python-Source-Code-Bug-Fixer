import numpy as np 

def function(x):

	w7 = x
	v6 = x
	x = x
	paths = []
	try:
		if v6 <= 6:
			v6 = v6+v6
			paths.append(1)
		else:
			x = w7/x
			v6 = 9-2
			paths.append(2)
		if v6 >= 2:
			w7 = w7/3
			v6 = v6-2
			paths.append(3)
		else:
			w7 = w7+x
			v6 = v6-1
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		w7 = v6**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))