import numpy as np 

def function(x):

	o2 = x
	w1 = x
	x = 7
	paths = []
	try:
		if w1 > 6:
			o2 = o2/3
			paths.append(1)
		else:
			w1 = w1+2
			x = x+w1
			x = 2+x
			paths.append(2)
		if w1 >= 5:
			o2 = o2/o2
			o2 = 9+w1
			x = 2/9
			paths.append(3)
		else:
			w1 = o2*w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))