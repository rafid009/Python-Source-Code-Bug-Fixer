import numpy as np 

def function(x):

	f2 = 7
	w2 = 2
	paths = []
	try:
		if f2 > 8:
			x = w2-x
			paths.append(1)
		else:
			x = x+f2
			paths.append(2)
		if w2 >= 7:
			x = 1-x
			w2 = w2-2
			paths.append(3)
		else:
			f2 = f2+f2
			f2 = f2/3
			w2 = 8-w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))