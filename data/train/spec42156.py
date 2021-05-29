import numpy as np 

def function(x):

	d6 = 4
	w7 = x
	x = 6
	paths = []
	try:
		if d6 > 1:
			d6 = w7-6
			w7 = 8+x
			paths.append(1)
		else:
			d6 = w7*d6
			d6 = 5/9
			paths.append(2)
		if d6 <= 3:
			w7 = w7*w7
			paths.append(3)
		else:
			w7 = w7/2
			d6 = 4/2
			x = 8/d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))