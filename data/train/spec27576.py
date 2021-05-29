import numpy as np 

def function(x):

	p8 = x
	r6 = x
	paths = []
	try:
		if x >= 5:
			x = x*3
			p8 = p8+6
			x = r6+4
			paths.append(1)
		else:
			p8 = p8+3
			paths.append(2)
		if x <= 8:
			x = x-0
			r6 = r6/x
			paths.append(3)
		else:
			r6 = 7*r6
			x = 5/9
			x = p8-8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		r6 = p8**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))