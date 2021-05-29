import numpy as np 

def function(x):

	w7 = x
	f2 = 2
	paths = []
	try:
		if f2 >= 4:
			f2 = x+f2
			paths.append(1)
		else:
			w7 = f2*w7
			w7 = 1-f2
			paths.append(2)
		if x >= 4:
			f2 = 6*f2
			paths.append(3)
		else:
			f2 = f2-f2
			w7 = f2+8
			w7 = w7*1
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