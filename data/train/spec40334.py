import numpy as np 

def function(x):

	v8 = x
	p4 = x
	paths = []
	try:
		if x >= 0:
			p4 = 6/3
			paths.append(1)
		else:
			x = x*7
			x = p4+x
			x = x+x
			paths.append(2)
		if v8 >= 8:
			x = 1-3
			v8 = v8-7
			x = x-8
			paths.append(3)
		else:
			v8 = 2+8
			v8 = p4+v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))