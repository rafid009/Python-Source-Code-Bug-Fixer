import numpy as np 

def function(x):

	w9 = 7
	y2 = 1
	paths = []
	try:
		if w9 <= 2:
			w9 = w9-8
			w9 = w9*4
			paths.append(1)
		else:
			w9 = y2/x
			x = x*x
			y2 = y2+7
			paths.append(2)
		if x > 0:
			x = x*1
			x = 2+x
			y2 = 5-y2
			paths.append(3)
		else:
			y2 = y2+y2
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