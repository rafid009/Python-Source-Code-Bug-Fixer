import numpy as np 

def function(x):

	a0 = x
	j6 = 0
	paths = []
	try:
		if j6 <= 8:
			j6 = j6+x
			paths.append(1)
		else:
			j6 = 2-j6
			a0 = a0+1
			paths.append(2)
		if j6 > 4:
			a0 = 4-x
			paths.append(3)
		else:
			a0 = a0+7
			a0 = 6*5
			j6 = a0*a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))