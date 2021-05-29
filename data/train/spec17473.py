import numpy as np 

def function(x):

	b2 = x
	w5 = x
	paths = []
	try:
		if w5 > 4:
			b2 = x/b2
			w5 = 9/5
			w5 = b2/2
			paths.append(1)
		else:
			b2 = b2+x
			w5 = 9+w5
			paths.append(2)
		if b2 <= 5:
			b2 = 3/b2
			w5 = 7-6
			b2 = b2*9
			paths.append(3)
		else:
			x = 9+1
			w5 = 3+w5
			x = w5-w5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))