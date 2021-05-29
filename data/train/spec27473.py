import numpy as np 

def function(x):

	i6 = 7
	l0 = x
	paths = []
	try:
		if l0 <= 0:
			l0 = x-i6
			x = 5*2
			paths.append(1)
		else:
			i6 = 8*i6
			i6 = i6+9
			paths.append(2)
		if i6 >= 8:
			x = 5-x
			l0 = 3-4
			paths.append(3)
		else:
			i6 = 9/i6
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))