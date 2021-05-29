import numpy as np 

def function(x):

	f5 = x
	w9 = x
	paths = []
	try:
		if w9 >= 7:
			f5 = 8/4
			paths.append(1)
		else:
			f5 = f5/2
			f5 = 0-f5
			paths.append(2)
		if w9 <= 4:
			x = x+f5
			x = 6/x
			paths.append(3)
		else:
			f5 = 8*f5
			x = x/x
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