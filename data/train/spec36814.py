import numpy as np 

def function(x):

	r3 = x
	i6 = x
	paths = []
	try:
		if i6 > 7:
			x = 2+0
			paths.append(1)
		else:
			r3 = r3-r3
			r3 = 7/x
			paths.append(2)
		if i6 <= 5:
			x = 2-x
			i6 = 8*i6
			i6 = i6+3
			paths.append(3)
		else:
			r3 = 2-6
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