import numpy as np 

def function(x):

	p8 = x
	o1 = x
	paths = []
	try:
		if p8 > 9:
			x = x+o1
			paths.append(1)
		else:
			o1 = o1-9
			paths.append(2)
		if x >= 9:
			x = x/6
			x = 5/7
			paths.append(3)
		else:
			o1 = 5-o1
			o1 = o1+p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))