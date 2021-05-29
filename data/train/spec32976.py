import numpy as np 

def function(x):

	p6 = 2
	o0 = 2
	paths = []
	try:
		if p6 <= 6:
			o0 = o0-7
			p6 = x/p6
			paths.append(1)
		else:
			p6 = 9*p6
			paths.append(2)
		if o0 >= 3:
			o0 = 2+2
			p6 = p6*4
			x = x*5
			paths.append(3)
		else:
			o0 = x/o0
			o0 = o0*4
			x = x+o0
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))