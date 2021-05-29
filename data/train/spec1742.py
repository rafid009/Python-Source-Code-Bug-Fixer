import numpy as np 

def function(x):

	t6 = 7
	w9 = x
	paths = []
	try:
		if x >= 2:
			w9 = t6-0
			paths.append(1)
		else:
			t6 = t6*4
			paths.append(2)
		if w9 >= 5:
			t6 = t6/1
			w9 = 2-3
			paths.append(3)
		else:
			w9 = 9-2
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))