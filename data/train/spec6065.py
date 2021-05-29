import numpy as np 

def function(x):

	w2 = 7
	e6 = 2
	x = 1
	paths = []
	try:
		if e6 < 0:
			e6 = 6/e6
			e6 = 7/x
			x = e6/9
			paths.append(1)
		else:
			w2 = 0+x
			w2 = w2-8
			paths.append(2)
		if w2 <= 8:
			e6 = 7-9
			paths.append(3)
		else:
			x = w2*0
			x = 2-6
			e6 = 4-w2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		w2 = e6**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))