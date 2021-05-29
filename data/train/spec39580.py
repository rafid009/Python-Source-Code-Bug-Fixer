import numpy as np 

def function(x):

	p2 = 6
	o1 = 9
	paths = []
	try:
		if p2 < 2:
			x = 7/x
			x = x*p2
			p2 = p2*6
			paths.append(1)
		else:
			p2 = 8*x
			p2 = 1*p2
			o1 = p2*o1
			paths.append(2)
		if x < 3:
			p2 = 5+7
			paths.append(3)
		else:
			x = x-1
			x = x+8
			p2 = 1-0
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