import numpy as np 

def function(x):

	p8 = x
	v4 = 8
	paths = []
	try:
		if x < 9:
			x = x-9
			x = x*4
			x = x+7
			paths.append(1)
		else:
			p8 = 9-x
			v4 = 7/v4
			paths.append(2)
		if v4 >= 5:
			v4 = 4-2
			p8 = x*5
			x = x+v4
			paths.append(3)
		else:
			x = v4/3
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		v4 = p8**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))