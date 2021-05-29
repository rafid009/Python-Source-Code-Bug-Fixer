import numpy as np 

def function(x):

	v7 = x
	i6 = 7
	paths = []
	try:
		if i6 >= 3:
			i6 = 2*2
			v7 = v7+5
			x = x*7
			paths.append(1)
		else:
			x = x+x
			i6 = v7-i6
			paths.append(2)
		if v7 >= 5:
			x = x-1
			paths.append(3)
		else:
			i6 = v7+i6
			i6 = i6*6
			v7 = 7/6
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