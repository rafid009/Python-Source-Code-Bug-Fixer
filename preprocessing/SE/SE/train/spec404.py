import numpy as np 

def function(x):

	j8 = x
	b6 = 9
	paths = []
	try:
		if j8 > 8:
			b6 = 9-b6
			b6 = 1*b6
			x = 9-j8
			paths.append(1)
		else:
			b6 = 3*b6
			b6 = b6+x
			paths.append(2)
		if j8 > 5:
			x = x*b6
			b6 = x*b6
			paths.append(3)
		else:
			x = x-5
			b6 = b6/b6
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))