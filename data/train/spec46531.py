import numpy as np 

def function(x):

	l9 = x
	i2 = x
	x = x
	paths = []
	try:
		if x <= 0:
			i2 = l9+x
			x = 9-x
			l9 = 1-x
			paths.append(1)
		else:
			l9 = 6-i2
			x = 2+x
			paths.append(2)
		if x < 8:
			l9 = l9-6
			i2 = i2-4
			l9 = i2/2
			paths.append(3)
		else:
			l9 = 3-l9
			l9 = 5+i2
			i2 = 1/l9
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		l9 = i2**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))