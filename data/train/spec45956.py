import numpy as np 

def function(x):

	w1 = x
	q5 = x
	paths = []
	try:
		if q5 <= 7:
			x = x/9
			paths.append(1)
		else:
			q5 = q5-9
			w1 = w1+6
			paths.append(2)
		if w1 < 8:
			q5 = q5-q5
			paths.append(3)
		else:
			w1 = q5-3
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))