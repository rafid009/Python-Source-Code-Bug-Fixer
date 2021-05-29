import numpy as np 

def function(x):

	v8 = 7
	g9 = 9
	paths = []
	try:
		if g9 > 5:
			x = 1*x
			x = x-7
			x = 9-x
			paths.append(1)
		else:
			x = 4/v8
			g9 = g9-4
			paths.append(2)
		if x <= 0:
			v8 = 9/x
			v8 = 3+v8
			paths.append(3)
		else:
			x = 6*2
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))