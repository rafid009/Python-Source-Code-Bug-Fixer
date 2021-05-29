import numpy as np 

def function(x):

	p6 = x
	r3 = x
	paths = []
	try:
		if r3 <= 2:
			r3 = r3/p6
			r3 = x-6
			r3 = r3-6
			paths.append(1)
		else:
			p6 = p6/7
			x = x+2
			paths.append(2)
		if p6 <= 3:
			r3 = 3-r3
			x = x*r3
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		r3 = p6**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))