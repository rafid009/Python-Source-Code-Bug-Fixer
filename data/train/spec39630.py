import numpy as np 

def function(x):

	n2 = 6
	w9 = x
	x = 9
	paths = []
	try:
		if n2 < 4:
			x = x*x
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if n2 <= 6:
			n2 = n2-n2
			w9 = 2-w9
			n2 = n2-4
			paths.append(3)
		else:
			n2 = 0+n2
			n2 = 0/n2
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