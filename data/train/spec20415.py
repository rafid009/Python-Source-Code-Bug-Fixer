import numpy as np 

def function(x):

	f7 = x
	w3 = 8
	paths = []
	try:
		if x <= 7:
			w3 = w3/w3
			paths.append(1)
		else:
			w3 = 1*w3
			f7 = f7*2
			paths.append(2)
		if w3 > 5:
			x = 7+f7
			w3 = f7+w3
			w3 = 3+w3
			paths.append(3)
		else:
			f7 = w3+f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))