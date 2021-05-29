import numpy as np 

def function(x):

	f9 = 3
	w7 = x
	paths = []
	try:
		if w7 <= 9:
			f9 = 0*f9
			f9 = w7*6
			paths.append(1)
		else:
			w7 = w7+2
			f9 = f9/4
			f9 = 0+w7
			paths.append(2)
		if w7 < 5:
			w7 = w7*6
			paths.append(3)
		else:
			f9 = 3*f9
			f9 = 2/9
			x = x/x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		w7 = f9**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))