import numpy as np 

def function(x):

	w2 = 6
	f9 = x
	paths = []
	try:
		if w2 < 6:
			w2 = w2+f9
			w2 = w2-w2
			paths.append(1)
		else:
			f9 = f9-7
			paths.append(2)
		if f9 < 6:
			x = 7-x
			f9 = f9-x
			paths.append(3)
		else:
			x = x+6
			f9 = 5/4
			w2 = f9-w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		f9 = w2**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))