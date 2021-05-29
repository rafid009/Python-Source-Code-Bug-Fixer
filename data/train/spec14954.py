import numpy as np 

def function(x):

	i8 = 3
	u3 = x
	paths = []
	try:
		if i8 <= 7:
			u3 = 5*8
			u3 = u3/6
			u3 = 2-u3
			paths.append(1)
		else:
			x = 9/x
			i8 = i8-5
			i8 = x*i8
			paths.append(2)
		if i8 < 2:
			u3 = u3+9
			u3 = i8/x
			paths.append(3)
		else:
			u3 = u3-2
			i8 = i8*x
			i8 = i8*i8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))