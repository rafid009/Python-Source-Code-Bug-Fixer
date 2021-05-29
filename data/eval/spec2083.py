import numpy as np 

def function(x):

	w2 = x
	r2 = 2
	paths = []
	try:
		if x < 0:
			x = 2/9
			paths.append(1)
		else:
			r2 = w2*3
			r2 = 3-r2
			paths.append(2)
		if r2 <= 4:
			r2 = 2/w2
			paths.append(3)
		else:
			w2 = w2+2
			w2 = x+w2
			x = x*w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))