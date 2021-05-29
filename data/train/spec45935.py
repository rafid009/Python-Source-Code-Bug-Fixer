import numpy as np 

def function(x):

	o6 = 8
	p7 = x
	paths = []
	try:
		if x >= 7:
			p7 = p7-1
			o6 = o6+o6
			x = 1*0
			paths.append(1)
		else:
			o6 = p7*x
			o6 = o6-2
			x = 1*x
			paths.append(2)
		if p7 >= 7:
			p7 = p7+4
			p7 = p7*p7
			x = 6-o6
			paths.append(3)
		else:
			x = x-p7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))