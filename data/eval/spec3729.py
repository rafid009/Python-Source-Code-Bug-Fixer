import numpy as np 

def function(x):

	f6 = x
	w2 = x
	paths = []
	try:
		if w2 > 3:
			x = 9+9
			w2 = 4-x
			x = 8+0
			paths.append(1)
		else:
			f6 = 7/f6
			paths.append(2)
		if x > 1:
			w2 = 7+6
			paths.append(3)
		else:
			f6 = f6/1
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		w2 = f6**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))