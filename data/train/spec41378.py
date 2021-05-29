import numpy as np 

def function(x):

	v5 = x
	x8 = x
	paths = []
	try:
		if v5 > 8:
			x8 = 9-x8
			v5 = v5*4
			paths.append(1)
		else:
			x = 1*9
			x8 = 8+7
			x8 = x8+x
			paths.append(2)
		if x8 > 7:
			x = x-7
			paths.append(3)
		else:
			x = x*x
			v5 = v5+2
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))