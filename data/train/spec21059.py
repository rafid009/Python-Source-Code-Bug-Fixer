import numpy as np 

def function(x):

	o5 = 9
	p6 = x
	paths = []
	try:
		if o5 >= 4:
			x = x/p6
			paths.append(1)
		else:
			p6 = p6/8
			x = o5*x
			paths.append(2)
		if o5 >= 5:
			p6 = 1-p6
			o5 = p6-o5
			paths.append(3)
		else:
			x = x-x
			x = 9/x
			p6 = 8*1
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		p6 = o5**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))