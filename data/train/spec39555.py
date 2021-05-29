import numpy as np 

def function(x):

	m2 = x
	w2 = 3
	paths = []
	try:
		if x < 2:
			w2 = w2/8
			paths.append(1)
		else:
			w2 = w2+1
			paths.append(2)
		if w2 > 5:
			w2 = 1/w2
			paths.append(3)
		else:
			w2 = w2-5
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