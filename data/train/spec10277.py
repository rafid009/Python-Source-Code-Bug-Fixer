import numpy as np 

def function(x):

	x6 = 7
	v9 = x
	paths = []
	try:
		if x6 < 7:
			v9 = v9/2
			paths.append(1)
		else:
			x = 6+x
			v9 = 3-v9
			v9 = 9+3
			paths.append(2)
		if x >= 5:
			x6 = 9+v9
			paths.append(3)
		else:
			x6 = 5*v9
			x6 = 5*4
			v9 = 4-x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x6 = v9**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))