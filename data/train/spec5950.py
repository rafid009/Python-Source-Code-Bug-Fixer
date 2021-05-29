import numpy as np 

def function(x):

	t8 = x
	l5 = 4
	paths = []
	try:
		if l5 < 4:
			l5 = l5*l5
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if t8 >= 6:
			l5 = l5/9
			paths.append(3)
		else:
			l5 = 2*8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))