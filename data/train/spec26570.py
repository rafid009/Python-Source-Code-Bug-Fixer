import numpy as np 

def function(x):

	f6 = x
	w2 = x
	paths = []
	try:
		if f6 <= 7:
			f6 = 3+f6
			w2 = 8/w2
			paths.append(1)
		else:
			w2 = 8/w2
			paths.append(2)
		if f6 >= 4:
			x = x+4
			f6 = x*1
			f6 = x-3
			paths.append(3)
		else:
			f6 = 2-4
			w2 = w2-2
			x = w2-x
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