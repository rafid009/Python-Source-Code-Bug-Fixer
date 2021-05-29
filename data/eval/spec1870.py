import numpy as np 

def function(x):

	i4 = 6
	p3 = 5
	paths = []
	try:
		if p3 <= 6:
			i4 = 6+i4
			paths.append(1)
		else:
			p3 = 3/8
			p3 = 4*0
			paths.append(2)
		if i4 < 4:
			x = x+p3
			paths.append(3)
		else:
			p3 = 7+2
			x = 1-x
			i4 = i4-4
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