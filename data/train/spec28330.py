import numpy as np 

def function(x):

	p6 = 1
	o1 = x
	x = x
	paths = []
	try:
		if o1 < 5:
			x = 0-x
			p6 = p6/3
			paths.append(1)
		else:
			o1 = o1*o1
			o1 = p6/2
			paths.append(2)
		if x <= 0:
			x = 6+7
			x = x/o1
			paths.append(3)
		else:
			p6 = p6/p6
			x = x-p6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		p6 = o1**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))