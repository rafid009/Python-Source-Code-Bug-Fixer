import numpy as np 

def function(x):

	o2 = 0
	w1 = 9
	x = 6
	paths = []
	try:
		if o2 <= 2:
			w1 = w1+0
			x = 2/x
			w1 = 0-x
			paths.append(1)
		else:
			w1 = 5/w1
			o2 = x+7
			x = 5-0
			paths.append(2)
		if w1 > 1:
			w1 = 8*w1
			o2 = x-x
			paths.append(3)
		else:
			x = 2-x
			o2 = x+o2
			w1 = w1*8
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))