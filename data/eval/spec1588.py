import numpy as np 

def function(x):

	v9 = x
	r3 = 3
	x = 5
	paths = []
	try:
		if v9 > 1:
			v9 = v9+5
			x = x-r3
			v9 = 9+2
			paths.append(1)
		else:
			r3 = 6+r3
			paths.append(2)
		if v9 < 0:
			v9 = v9*4
			paths.append(3)
		else:
			x = 4*5
			r3 = 7*r3
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