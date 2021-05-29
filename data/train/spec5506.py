import numpy as np 

def function(x):

	q6 = x
	w2 = x
	paths = []
	try:
		if w2 < 2:
			x = x+6
			w2 = x-w2
			x = x*9
			paths.append(1)
		else:
			x = 5/5
			q6 = q6/3
			paths.append(2)
		if q6 < 7:
			w2 = w2+x
			w2 = w2/x
			paths.append(3)
		else:
			w2 = 3*0
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