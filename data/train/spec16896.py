import numpy as np 

def function(x):

	w6 = 2
	d5 = x
	paths = []
	try:
		if x < 7:
			w6 = x/w6
			paths.append(1)
		else:
			w6 = 0*0
			paths.append(2)
		if x < 3:
			w6 = w6*x
			w6 = 1*w6
			x = 0-w6
			paths.append(3)
		else:
			x = x+9
			d5 = d5-w6
			x = d5/x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))