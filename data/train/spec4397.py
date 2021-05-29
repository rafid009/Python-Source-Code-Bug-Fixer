import numpy as np 

def function(x):

	o4 = 4
	n2 = 2
	paths = []
	try:
		if o4 > 9:
			o4 = o4+x
			paths.append(1)
		else:
			o4 = n2-8
			n2 = n2-5
			paths.append(2)
		if x > 7:
			n2 = 9-n2
			o4 = o4*5
			paths.append(3)
		else:
			o4 = o4/7
			o4 = o4*1
			o4 = o4-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))