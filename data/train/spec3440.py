import numpy as np 

def function(x):

	x7 = x
	v7 = x
	paths = []
	try:
		if x <= 7:
			x = x*7
			x7 = x7*3
			v7 = x*6
			paths.append(1)
		else:
			x = x*2
			x = 2+9
			x7 = 6+x7
			paths.append(2)
		if v7 <= 4:
			v7 = v7*v7
			paths.append(3)
		else:
			v7 = v7+6
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))