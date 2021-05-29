import numpy as np 

def function(x):

	d6 = x
	w7 = 0
	paths = []
	try:
		if w7 <= 3:
			w7 = d6/d6
			w7 = 2/w7
			paths.append(1)
		else:
			x = 4/x
			w7 = 3/9
			w7 = 8+w7
			paths.append(2)
		if d6 > 3:
			d6 = d6+d6
			paths.append(3)
		else:
			w7 = 4*d6
			d6 = 0*1
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))