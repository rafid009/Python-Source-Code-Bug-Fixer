import numpy as np 

def function(x):

	w6 = 4
	i8 = x
	paths = []
	try:
		if i8 >= 6:
			w6 = 3+w6
			paths.append(1)
		else:
			w6 = w6/i8
			i8 = x/i8
			paths.append(2)
		if w6 >= 8:
			i8 = 7+0
			paths.append(3)
		else:
			i8 = i8+4
			i8 = 5/7
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))