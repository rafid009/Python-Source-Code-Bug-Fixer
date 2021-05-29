import numpy as np 

def function(x):

	l0 = x
	v3 = x
	paths = []
	try:
		if v3 > 9:
			l0 = l0-7
			l0 = 9-x
			paths.append(1)
		else:
			v3 = 0/v3
			v3 = v3-x
			paths.append(2)
		if v3 <= 5:
			l0 = l0*8
			x = x-1
			l0 = l0-9
			paths.append(3)
		else:
			l0 = x*7
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		l0 = v3**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))