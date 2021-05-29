import numpy as np 

def function(x):

	w2 = x
	l5 = 3
	paths = []
	try:
		if x > 9:
			x = 6*0
			l5 = l5/5
			x = 6+x
			paths.append(1)
		else:
			x = x-4
			x = x/8
			paths.append(2)
		if x <= 0:
			l5 = l5*9
			paths.append(3)
		else:
			x = x-x
			l5 = l5-4
			w2 = w2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))