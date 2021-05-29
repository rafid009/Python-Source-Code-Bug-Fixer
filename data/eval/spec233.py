import numpy as np 

def function(x):

	f8 = 8
	w9 = x
	paths = []
	try:
		if w9 < 7:
			w9 = 6/w9
			x = x*4
			paths.append(1)
		else:
			f8 = f8/f8
			f8 = f8+f8
			paths.append(2)
		if f8 > 5:
			f8 = f8+f8
			x = f8/x
			paths.append(3)
		else:
			f8 = x+f8
			f8 = f8+x
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