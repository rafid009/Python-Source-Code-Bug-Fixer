import numpy as np 

def function(x):

	o1 = 4
	p1 = x
	paths = []
	try:
		if o1 > 3:
			p1 = p1*6
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if o1 <= 5:
			p1 = p1-1
			p1 = p1/4
			o1 = 3+0
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		o1 = p1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))