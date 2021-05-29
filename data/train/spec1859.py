import numpy as np 

def function(x):

	w9 = x
	v6 = 5
	paths = []
	try:
		if w9 <= 8:
			v6 = v6/v6
			paths.append(1)
		else:
			w9 = 5/w9
			paths.append(2)
		if w9 < 5:
			v6 = 5/v6
			v6 = 3-v6
			paths.append(3)
		else:
			w9 = 6/x
			w9 = v6/x
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