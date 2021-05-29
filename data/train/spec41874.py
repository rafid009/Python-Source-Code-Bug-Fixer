import numpy as np 

def function(x):

	f3 = 7
	v8 = x
	paths = []
	try:
		if v8 <= 0:
			f3 = f3/2
			x = 4/x
			paths.append(1)
		else:
			v8 = 5*x
			v8 = v8+6
			paths.append(2)
		if v8 <= 9:
			v8 = v8-4
			paths.append(3)
		else:
			x = 1+7
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