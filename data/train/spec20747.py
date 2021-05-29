import numpy as np 

def function(x):

	a6 = 2
	j8 = 1
	paths = []
	try:
		if a6 >= 0:
			x = a6+x
			x = 1-4
			x = 5+1
			paths.append(1)
		else:
			x = x+2
			x = 3-x
			a6 = 9/2
			paths.append(2)
		if j8 <= 8:
			j8 = j8+x
			a6 = 6*j8
			a6 = 5-a6
			paths.append(3)
		else:
			a6 = 5*a6
			x = x*9
			x = 3-j8
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		j8 = a6**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))