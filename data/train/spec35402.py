import numpy as np 

def function(x):

	r2 = 1
	v9 = 7
	paths = []
	try:
		if x <= 5:
			r2 = 6-8
			paths.append(1)
		else:
			v9 = v9/6
			x = v9*r2
			x = 8+x
			paths.append(2)
		if v9 > 2:
			x = 3/x
			r2 = r2/r2
			v9 = v9+7
			paths.append(3)
		else:
			x = 1+5
			r2 = 0*x
			v9 = 6-9
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