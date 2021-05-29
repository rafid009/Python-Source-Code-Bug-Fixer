import numpy as np 

def function(x):

	l3 = 9
	i6 = x
	paths = []
	try:
		if l3 < 6:
			i6 = i6*8
			i6 = 4+i6
			l3 = 9-l3
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if i6 < 6:
			x = x/2
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))