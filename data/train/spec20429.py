import numpy as np 

def function(x):

	f4 = 4
	w1 = x
	paths = []
	try:
		if w1 <= 3:
			w1 = w1-8
			f4 = f4-x
			x = x+6
			paths.append(1)
		else:
			f4 = f4-9
			paths.append(2)
		if w1 < 2:
			x = 7+x
			paths.append(3)
		else:
			w1 = 9-w1
			f4 = f4+0
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		f4 = w1**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))