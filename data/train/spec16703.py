import numpy as np 

def function(x):

	f0 = 6
	w7 = x
	paths = []
	try:
		if w7 >= 4:
			x = x/f0
			paths.append(1)
		else:
			x = 5-x
			f0 = f0*7
			paths.append(2)
		if x <= 9:
			x = x+w7
			w7 = 7+1
			paths.append(3)
		else:
			w7 = w7/2
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		f0 = w7**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))