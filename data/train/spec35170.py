import numpy as np 

def function(x):

	w6 = 6
	b9 = x
	paths = []
	try:
		if w6 > 5:
			x = x+4
			paths.append(1)
		else:
			b9 = 7-b9
			b9 = 0+3
			w6 = w6*3
			paths.append(2)
		if w6 < 6:
			x = x*x
			paths.append(3)
		else:
			w6 = 2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))