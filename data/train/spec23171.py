import numpy as np 

def function(x):

	a7 = 1
	v8 = x
	x = 7
	paths = []
	try:
		if x > 0:
			a7 = 2-a7
			v8 = v8/3
			x = x/9
			paths.append(1)
		else:
			x = 2/8
			paths.append(2)
		if x > 8:
			x = x*6
			a7 = x/a7
			paths.append(3)
		else:
			a7 = 4+a7
			v8 = v8/a7
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))