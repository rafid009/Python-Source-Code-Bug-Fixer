import numpy as np 

def function(x):

	p3 = 5
	w9 = x
	paths = []
	try:
		if p3 < 1:
			w9 = 9+w9
			paths.append(1)
		else:
			x = x/5
			p3 = p3+w9
			paths.append(2)
		if x > 6:
			p3 = w9+2
			p3 = p3/p3
			p3 = p3*9
			paths.append(3)
		else:
			p3 = x/p3
			w9 = w9+p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		w9 = p3**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))