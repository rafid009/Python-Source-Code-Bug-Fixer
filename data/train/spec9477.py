import numpy as np 

def function(x):

	w9 = 8
	f6 = 4
	paths = []
	try:
		if x >= 0:
			x = f6-f6
			w9 = w9/f6
			paths.append(1)
		else:
			f6 = w9/7
			w9 = x/f6
			paths.append(2)
		if f6 <= 5:
			f6 = f6*8
			paths.append(3)
		else:
			w9 = 3/w9
			w9 = w9/w9
			f6 = 6+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))