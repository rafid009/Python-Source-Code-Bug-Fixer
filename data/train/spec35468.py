import numpy as np 

def function(x):

	i4 = 3
	p1 = 1
	paths = []
	try:
		if x > 3:
			p1 = p1+7
			x = x*x
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if i4 < 3:
			i4 = i4/3
			paths.append(3)
		else:
			i4 = x-9
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))