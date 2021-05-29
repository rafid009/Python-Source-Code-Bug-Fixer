import numpy as np 

def function(x):

	p3 = 7
	o2 = x
	paths = []
	try:
		if p3 < 0:
			o2 = o2+9
			paths.append(1)
		else:
			o2 = o2*7
			paths.append(2)
		if p3 > 2:
			x = 5+x
			paths.append(3)
		else:
			p3 = p3+3
			x = o2-x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))