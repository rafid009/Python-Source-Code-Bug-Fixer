import numpy as np 

def function(x):

	f4 = x
	w2 = 9
	paths = []
	try:
		if x > 4:
			w2 = 7-w2
			f4 = f4/f4
			w2 = 4/w2
			paths.append(1)
		else:
			w2 = w2/4
			paths.append(2)
		if x > 2:
			f4 = w2-x
			f4 = w2-6
			x = x+w2
			paths.append(3)
		else:
			x = 9-6
			w2 = w2-x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))