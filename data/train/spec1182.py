import numpy as np 

def function(x):

	b5 = x
	w6 = 9
	paths = []
	try:
		if x > 2:
			w6 = w6*b5
			w6 = w6*3
			x = x*7
			paths.append(1)
		else:
			b5 = b5+b5
			x = x/b5
			paths.append(2)
		if b5 < 1:
			b5 = b5-6
			w6 = w6+x
			paths.append(3)
		else:
			b5 = w6-b5
			x = x/b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		w6 = b5**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))