import numpy as np 

def function(x):

	d1 = 9
	w2 = x
	paths = []
	try:
		if x <= 8:
			d1 = 2/d1
			w2 = w2+2
			d1 = 9/w2
			paths.append(1)
		else:
			d1 = w2-d1
			paths.append(2)
		if x < 5:
			x = x/x
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		w2 = d1**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))