import numpy as np 

def function(x):

	u4 = 9
	a3 = 9
	x = x
	paths = []
	try:
		if x < 3:
			a3 = x*a3
			a3 = a3+u4
			u4 = a3-u4
			paths.append(1)
		else:
			a3 = a3+0
			paths.append(2)
		if u4 > 5:
			a3 = a3-9
			paths.append(3)
		else:
			u4 = x+u4
			a3 = a3+1
			a3 = x-0
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