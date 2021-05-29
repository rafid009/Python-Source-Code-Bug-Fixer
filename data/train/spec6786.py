import numpy as np 

def function(x):

	w6 = 3
	l9 = 2
	paths = []
	try:
		if x < 7:
			w6 = x-l9
			paths.append(1)
		else:
			w6 = 9*w6
			paths.append(2)
		if l9 < 5:
			l9 = l9/8
			paths.append(3)
		else:
			x = 5*1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))