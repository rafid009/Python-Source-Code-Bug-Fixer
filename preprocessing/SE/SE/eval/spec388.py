import numpy as np 

def function(x):

	v8 = x
	l8 = x
	x = 9
	paths = []
	try:
		if l8 >= 7:
			x = 7+1
			x = x-3
			l8 = l8+v8
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if v8 >= 7:
			x = x-7
			x = 4+x
			paths.append(3)
		else:
			x = 5*x
			v8 = v8+x
			l8 = l8/v8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		v8 = l8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))