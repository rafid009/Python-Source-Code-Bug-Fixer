import numpy as np 

def function(x):

	d6 = 3
	w2 = 3
	paths = []
	try:
		if x > 1:
			w2 = 2/8
			d6 = d6-7
			x = 2+x
			paths.append(1)
		else:
			d6 = 6-6
			d6 = w2*1
			d6 = x/d6
			paths.append(2)
		if x <= 1:
			w2 = w2+x
			paths.append(3)
		else:
			d6 = d6+x
			d6 = d6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))