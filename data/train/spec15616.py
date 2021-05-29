import numpy as np 

def function(x):

	o7 = 4
	p3 = x
	paths = []
	try:
		if p3 <= 9:
			p3 = p3-6
			o7 = p3-o7
			paths.append(1)
		else:
			o7 = 3+p3
			paths.append(2)
		if p3 >= 7:
			o7 = o7+8
			p3 = p3*o7
			paths.append(3)
		else:
			o7 = o7*p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))