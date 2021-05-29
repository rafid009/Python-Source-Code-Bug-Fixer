import numpy as np 

def function(x):

	b5 = x
	w6 = 9
	paths = []
	try:
		if b5 <= 8:
			b5 = b5/x
			w6 = x+w6
			paths.append(1)
		else:
			b5 = w6-b5
			paths.append(2)
		if x < 2:
			b5 = b5/2
			x = x-3
			paths.append(3)
		else:
			b5 = 1-b5
			b5 = b5*5
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