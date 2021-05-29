import numpy as np 

def function(x):

	b8 = x
	v4 = x
	paths = []
	try:
		if v4 >= 7:
			x = x/v4
			paths.append(1)
		else:
			v4 = v4/8
			v4 = 5+b8
			paths.append(2)
		if x < 5:
			v4 = v4/8
			paths.append(3)
		else:
			x = 2+3
			x = x/7
			b8 = 0+4
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		v4 = b8**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))