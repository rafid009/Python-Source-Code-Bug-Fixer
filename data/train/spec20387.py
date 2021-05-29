import numpy as np 

def function(x):

	w2 = 2
	b6 = 3
	paths = []
	try:
		if x > 8:
			b6 = 9/b6
			w2 = w2*9
			w2 = 1+1
			paths.append(1)
		else:
			w2 = 7-w2
			b6 = b6*2
			b6 = b6/b6
			paths.append(2)
		if x > 4:
			x = 8/9
			w2 = 8*0
			paths.append(3)
		else:
			w2 = x*5
			x = x*9
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