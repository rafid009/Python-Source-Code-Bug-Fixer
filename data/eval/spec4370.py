import numpy as np 

def function(x):

	i0 = 9
	w2 = x
	paths = []
	try:
		if w2 < 5:
			i0 = x/i0
			x = x/5
			paths.append(1)
		else:
			x = x/w2
			x = x+i0
			paths.append(2)
		if x <= 6:
			w2 = 9/6
			w2 = w2-8
			x = 5*x
			paths.append(3)
		else:
			i0 = i0+x
			i0 = x-2
			i0 = 2-i0
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