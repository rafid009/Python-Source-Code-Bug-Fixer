import numpy as np 

def function(x):

	i6 = x
	l0 = 1
	paths = []
	try:
		if i6 >= 1:
			i6 = i6*0
			l0 = 2+l0
			i6 = i6-6
			paths.append(1)
		else:
			l0 = l0-0
			paths.append(2)
		if x <= 5:
			i6 = 1+x
			paths.append(3)
		else:
			x = 8-i6
			i6 = 2/i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))