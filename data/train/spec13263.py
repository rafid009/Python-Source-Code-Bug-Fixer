import numpy as np 

def function(x):

	d8 = 8
	w1 = x
	paths = []
	try:
		if x <= 8:
			d8 = x*w1
			paths.append(1)
		else:
			x = w1+x
			w1 = 1+2
			paths.append(2)
		if w1 > 5:
			d8 = d8/6
			w1 = 5/w1
			paths.append(3)
		else:
			x = 1*w1
			x = x+5
			d8 = x-w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))