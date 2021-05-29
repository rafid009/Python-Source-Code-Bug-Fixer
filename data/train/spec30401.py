import numpy as np 

def function(x):

	w2 = 5
	p9 = 8
	paths = []
	try:
		if x >= 9:
			x = 8-8
			x = x*6
			w2 = w2+x
			paths.append(1)
		else:
			w2 = w2/x
			p9 = p9-x
			paths.append(2)
		if w2 < 0:
			p9 = 9*6
			paths.append(3)
		else:
			p9 = p9/4
			w2 = 2*w2
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		w2 = p9**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))