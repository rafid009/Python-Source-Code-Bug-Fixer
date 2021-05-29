import numpy as np 

def function(x):

	f6 = 5
	w9 = x
	x = x
	paths = []
	try:
		if w9 > 9:
			x = x/w9
			f6 = w9+f6
			w9 = w9-2
			paths.append(1)
		else:
			w9 = w9/w9
			w9 = w9+1
			paths.append(2)
		if w9 <= 0:
			f6 = w9*f6
			paths.append(3)
		else:
			f6 = x+w9
			f6 = x+f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		w9 = f6**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))