import numpy as np 

def function(x):

	o1 = x
	l9 = 3
	x = x
	paths = []
	try:
		if o1 <= 4:
			x = 5+x
			paths.append(1)
		else:
			o1 = 1/8
			l9 = 4+l9
			o1 = o1-9
			paths.append(2)
		if l9 >= 8:
			l9 = l9-5
			paths.append(3)
		else:
			l9 = o1/o1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))