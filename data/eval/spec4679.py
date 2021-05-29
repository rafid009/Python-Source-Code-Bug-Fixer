import numpy as np 

def function(x):

	w1 = 5
	p8 = 4
	paths = []
	try:
		if w1 <= 8:
			x = x/6
			w1 = w1-8
			paths.append(1)
		else:
			x = 8-7
			paths.append(2)
		if p8 < 7:
			x = x/6
			w1 = w1*8
			paths.append(3)
		else:
			x = 8-x
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