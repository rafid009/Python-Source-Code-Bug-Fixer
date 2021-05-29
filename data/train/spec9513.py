import numpy as np 

def function(x):

	j4 = x
	a3 = 9
	paths = []
	try:
		if x <= 0:
			a3 = 3*x
			paths.append(1)
		else:
			a3 = x*a3
			x = x*2
			a3 = a3*3
			paths.append(2)
		if a3 < 9:
			x = x-2
			j4 = j4*0
			paths.append(3)
		else:
			a3 = j4-x
			x = x/8
			x = x-7
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))