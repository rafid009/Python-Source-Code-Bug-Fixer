import numpy as np 

def function(x):

	f7 = 6
	w9 = x
	paths = []
	try:
		if x >= 4:
			w9 = 7+f7
			x = 7+x
			w9 = 4-8
			paths.append(1)
		else:
			x = x+1
			w9 = 0+w9
			f7 = f7/4
			paths.append(2)
		if w9 >= 1:
			f7 = 7/6
			f7 = 3-w9
			f7 = 8/4
			paths.append(3)
		else:
			x = x/w9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))