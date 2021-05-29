import numpy as np 

def function(x):

	l0 = 0
	i6 = 6
	x = 5
	paths = []
	try:
		if l0 <= 1:
			l0 = l0*9
			i6 = 1-i6
			x = x*i6
			paths.append(1)
		else:
			l0 = 7+3
			paths.append(2)
		if l0 < 6:
			x = 1+x
			paths.append(3)
		else:
			x = x-8
			l0 = l0-0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		l0 = i6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))