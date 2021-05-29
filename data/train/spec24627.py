import numpy as np 

def function(x):

	y5 = 4
	v3 = 0
	x = 6
	paths = []
	try:
		if y5 > 9:
			x = 9/x
			paths.append(1)
		else:
			x = x-2
			v3 = 2-8
			y5 = y5*1
			paths.append(2)
		if v3 > 5:
			y5 = 6-y5
			v3 = 3-8
			paths.append(3)
		else:
			v3 = v3+x
			v3 = v3*8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))