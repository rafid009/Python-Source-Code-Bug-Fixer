import numpy as np 

def function(x):

	v2 = 3
	e6 = x
	x = 2
	paths = []
	try:
		if x > 4:
			v2 = v2/7
			v2 = e6/6
			paths.append(1)
		else:
			v2 = 9*4
			v2 = 5+0
			paths.append(2)
		if v2 > 5:
			e6 = v2-x
			e6 = 8+e6
			paths.append(3)
		else:
			v2 = v2-8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))