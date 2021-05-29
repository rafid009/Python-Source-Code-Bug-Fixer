import numpy as np 

def function(x):

	i6 = x
	w9 = 6
	paths = []
	try:
		if i6 < 8:
			w9 = 5+w9
			i6 = 3+i6
			paths.append(1)
		else:
			w9 = w9*3
			i6 = i6+0
			paths.append(2)
		if i6 <= 6:
			w9 = 9-w9
			paths.append(3)
		else:
			x = 2*6
			w9 = w9-0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))