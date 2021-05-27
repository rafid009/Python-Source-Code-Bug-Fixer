import numpy as np 

def function(x):

	w2 = x
	f2 = 2
	paths = []
	try:
		if f2 > 9:
			w2 = w2+9
			paths.append(1)
		else:
			x = 4+w2
			paths.append(2)
		if f2 >= 1:
			f2 = f2-7
			f2 = w2*w2
			w2 = w2+f2
			paths.append(3)
		else:
			w2 = w2*w2
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