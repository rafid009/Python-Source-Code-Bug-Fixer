import numpy as np 

def function(x):

	e1 = x
	i8 = 2
	x = x
	paths = []
	try:
		if e1 > 3:
			i8 = 0+i8
			paths.append(1)
		else:
			i8 = i8-e1
			x = x+i8
			paths.append(2)
		if e1 >= 9:
			x = i8+x
			x = 6+2
			paths.append(3)
		else:
			x = x+2
			e1 = e1-1
			i8 = 8-i8
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))