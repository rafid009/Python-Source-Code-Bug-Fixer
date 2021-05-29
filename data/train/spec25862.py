import numpy as np 

def function(x):

	n0 = 1
	v9 = x
	x = 9
	paths = []
	try:
		if x > 2:
			n0 = n0/5
			paths.append(1)
		else:
			v9 = 4+n0
			x = x+n0
			x = 5-9
			paths.append(2)
		if n0 <= 6:
			v9 = 0+v9
			n0 = x/n0
			paths.append(3)
		else:
			v9 = 1*0
			n0 = n0-4
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))