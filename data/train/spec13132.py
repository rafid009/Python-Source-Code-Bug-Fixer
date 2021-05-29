import numpy as np 

def function(x):

	u9 = x
	w7 = 2
	paths = []
	try:
		if u9 < 9:
			w7 = u9-w7
			w7 = w7/1
			paths.append(1)
		else:
			u9 = u9*0
			x = x*3
			w7 = 7*u9
			paths.append(2)
		if w7 < 4:
			w7 = 8+9
			paths.append(3)
		else:
			w7 = 6+5
			x = x*u9
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))