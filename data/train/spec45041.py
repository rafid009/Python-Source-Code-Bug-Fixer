import numpy as np 

def function(x):

	f8 = 9
	w2 = 1
	paths = []
	try:
		if w2 > 6:
			f8 = x+f8
			paths.append(1)
		else:
			f8 = 8*x
			paths.append(2)
		if x >= 3:
			f8 = w2*w2
			paths.append(3)
		else:
			f8 = f8/7
			x = x*2
			w2 = w2*w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))