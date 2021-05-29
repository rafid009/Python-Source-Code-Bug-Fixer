import numpy as np 

def function(x):

	o4 = 2
	p6 = x
	x = x
	paths = []
	try:
		if o4 < 0:
			o4 = 5/6
			paths.append(1)
		else:
			o4 = o4-1
			o4 = 9+8
			paths.append(2)
		if p6 >= 2:
			p6 = p6+0
			p6 = p6/3
			paths.append(3)
		else:
			p6 = x/7
			p6 = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))