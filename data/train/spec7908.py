import numpy as np 

def function(x):

	w1 = 0
	o1 = x
	paths = []
	try:
		if w1 < 5:
			x = 1/4
			paths.append(1)
		else:
			o1 = 4/7
			paths.append(2)
		if w1 <= 9:
			x = o1+x
			o1 = 4*o1
			paths.append(3)
		else:
			o1 = o1-2
			x = x*x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))