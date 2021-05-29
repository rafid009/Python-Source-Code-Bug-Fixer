import numpy as np 

def function(x):

	v7 = 9
	v2 = x
	paths = []
	try:
		if v2 <= 7:
			v2 = 5-v2
			x = v2*5
			v7 = v7*2
			paths.append(1)
		else:
			v2 = v2+0
			v2 = v7/3
			paths.append(2)
		if v2 > 7:
			x = 2-x
			x = v7+x
			paths.append(3)
		else:
			v2 = 2+v2
			x = v7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))