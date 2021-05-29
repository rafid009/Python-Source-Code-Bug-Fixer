import numpy as np 

def function(x):

	q6 = x
	w2 = x
	paths = []
	try:
		if q6 < 4:
			x = 8+x
			x = w2-5
			q6 = q6*3
			paths.append(1)
		else:
			w2 = w2*4
			x = 0-9
			paths.append(2)
		if x >= 6:
			q6 = q6*2
			paths.append(3)
		else:
			w2 = 9-q6
			q6 = x+q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		w2 = q6**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))