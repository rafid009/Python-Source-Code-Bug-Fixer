import numpy as np 

def function(x):

	v3 = 2
	l5 = 8
	paths = []
	try:
		if l5 >= 6:
			v3 = 0/v3
			l5 = l5/l5
			paths.append(1)
		else:
			x = v3-x
			paths.append(2)
		if l5 < 8:
			v3 = v3-7
			paths.append(3)
		else:
			v3 = v3/2
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		l5 = v3**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))