import numpy as np 

def function(x):

	q2 = x
	w2 = 8
	paths = []
	try:
		if x <= 9:
			x = x/5
			paths.append(1)
		else:
			q2 = q2-q2
			x = x-3
			q2 = 3-4
			paths.append(2)
		if w2 <= 3:
			q2 = 1+q2
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		w2 = q2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))