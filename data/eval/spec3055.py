import numpy as np 

def function(x):

	w1 = x
	t5 = 8
	x = x
	paths = []
	try:
		if w1 >= 2:
			w1 = x/5
			paths.append(1)
		else:
			t5 = 2-x
			x = 5*5
			paths.append(2)
		if t5 < 8:
			x = 2-1
			w1 = 4+1
			w1 = t5/t5
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))