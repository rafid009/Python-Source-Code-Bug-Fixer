import numpy as np 

def function(x):

	p6 = x
	w7 = 5
	paths = []
	try:
		if w7 < 0:
			x = p6*x
			paths.append(1)
		else:
			x = 3-2
			paths.append(2)
		if x <= 5:
			x = x/p6
			p6 = w7+p6
			paths.append(3)
		else:
			x = 2*p6
			p6 = p6+1
			w7 = 5/w7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		w7 = p6**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))