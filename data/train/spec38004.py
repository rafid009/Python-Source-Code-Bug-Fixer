import numpy as np 

def function(x):

	p1 = x
	i8 = x
	x = 3
	paths = []
	try:
		if p1 >= 6:
			p1 = p1*4
			paths.append(1)
		else:
			i8 = 4-2
			paths.append(2)
		if i8 >= 5:
			x = x-p1
			paths.append(3)
		else:
			x = x*8
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))