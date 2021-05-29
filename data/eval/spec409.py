import numpy as np 

def function(x):

	o1 = 8
	p7 = 9
	paths = []
	try:
		if x > 4:
			x = x*p7
			paths.append(1)
		else:
			o1 = 1/x
			paths.append(2)
		if o1 > 2:
			p7 = 2+0
			paths.append(3)
		else:
			o1 = x+0
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