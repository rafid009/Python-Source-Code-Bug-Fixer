import numpy as np 

def function(x):

	v3 = 2
	i7 = 0
	paths = []
	try:
		if i7 < 7:
			v3 = v3*4
			paths.append(1)
		else:
			v3 = v3/v3
			paths.append(2)
		if x < 1:
			v3 = 5/x
			x = x*5
			x = 4+x
			paths.append(3)
		else:
			x = 5/x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))