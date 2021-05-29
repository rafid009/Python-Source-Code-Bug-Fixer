import numpy as np 

def function(x):

	x0 = 2
	v9 = 2
	paths = []
	try:
		if v9 > 0:
			x = 3+1
			x = 3/x
			x = x+x
			paths.append(1)
		else:
			x = x/4
			x0 = 5/x0
			paths.append(2)
		if x >= 5:
			v9 = v9+0
			paths.append(3)
		else:
			x = x+8
			v9 = v9-9
			x = x+5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))