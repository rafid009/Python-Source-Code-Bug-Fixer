import numpy as np 

def function(x):

	x2 = 3
	v8 = 3
	x = x
	paths = []
	try:
		if v8 > 7:
			v8 = x-9
			x2 = x2*5
			paths.append(1)
		else:
			v8 = x/x
			x2 = x*x2
			paths.append(2)
		if x > 6:
			x = 0*v8
			paths.append(3)
		else:
			v8 = x2+x
			v8 = 0-x2
			x = x/4
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