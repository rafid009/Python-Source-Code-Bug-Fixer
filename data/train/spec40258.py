import numpy as np 

def function(x):

	v9 = 3
	a4 = x
	paths = []
	try:
		if x <= 2:
			x = 0+x
			x = x*6
			paths.append(1)
		else:
			v9 = 5-x
			a4 = 5/8
			x = x/x
			paths.append(2)
		if v9 <= 7:
			a4 = a4-x
			a4 = a4-1
			paths.append(3)
		else:
			v9 = v9/x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		a4 = v9**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))