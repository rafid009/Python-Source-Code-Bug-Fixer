import numpy as np 

def function(x):

	d5 = x
	w9 = 4
	paths = []
	try:
		if d5 <= 3:
			d5 = d5+4
			d5 = 4/d5
			x = x*3
			paths.append(1)
		else:
			w9 = x+7
			x = 5-x
			x = x+7
			paths.append(2)
		if x >= 9:
			d5 = d5/7
			paths.append(3)
		else:
			d5 = d5/6
			d5 = x-d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		w9 = d5**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))