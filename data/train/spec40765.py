import numpy as np 

def function(x):

	v3 = x
	r2 = 1
	paths = []
	try:
		if v3 < 6:
			r2 = r2-x
			paths.append(1)
		else:
			x = x/6
			x = 3/4
			r2 = 8*x
			paths.append(2)
		if v3 <= 8:
			v3 = v3-0
			x = x*x
			paths.append(3)
		else:
			x = x+v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))