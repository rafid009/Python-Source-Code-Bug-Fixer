import numpy as np 

def function(x):

	a9 = x
	j8 = 7
	paths = []
	try:
		if x >= 3:
			j8 = j8+7
			j8 = j8*a9
			x = x/a9
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if x >= 2:
			x = 5+x
			x = 6*x
			paths.append(3)
		else:
			j8 = 0*x
			x = x/5
			j8 = j8*0
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))