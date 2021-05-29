import numpy as np 

def function(x):

	e9 = 1
	j0 = x
	paths = []
	try:
		if e9 >= 6:
			x = x*e9
			j0 = j0*0
			x = x/5
			paths.append(1)
		else:
			j0 = j0*5
			j0 = 5/j0
			x = x/e9
			paths.append(2)
		if e9 > 8:
			j0 = j0+9
			e9 = 8*6
			j0 = 5+j0
			paths.append(3)
		else:
			x = 4-x
			x = x/9
			e9 = 3*x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))