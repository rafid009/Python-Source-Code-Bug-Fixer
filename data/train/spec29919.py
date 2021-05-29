import numpy as np 

def function(x):

	w9 = 6
	l0 = 6
	paths = []
	try:
		if l0 < 8:
			l0 = 9/l0
			paths.append(1)
		else:
			l0 = 0+4
			paths.append(2)
		if w9 < 1:
			l0 = 6+l0
			x = 1+x
			paths.append(3)
		else:
			w9 = x/9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))