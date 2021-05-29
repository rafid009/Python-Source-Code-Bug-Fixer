import numpy as np 

def function(x):

	a4 = x
	i6 = 9
	paths = []
	try:
		if a4 < 3:
			x = i6-i6
			a4 = a4/9
			x = x*9
			paths.append(1)
		else:
			x = 6/7
			x = 3-i6
			i6 = 2*8
			paths.append(2)
		if x >= 2:
			a4 = a4+a4
			x = 6*x
			paths.append(3)
		else:
			i6 = a4/a4
			x = x+i6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))