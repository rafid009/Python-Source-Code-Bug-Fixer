import numpy as np 

def function(x):

	w1 = x
	e2 = 4
	paths = []
	try:
		if e2 > 5:
			w1 = w1/7
			paths.append(1)
		else:
			e2 = e2+5
			w1 = w1/x
			w1 = 3*w1
			paths.append(2)
		if w1 <= 4:
			e2 = 5/5
			e2 = w1-e2
			e2 = e2-5
			paths.append(3)
		else:
			e2 = e2-w1
			w1 = 6-9
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))