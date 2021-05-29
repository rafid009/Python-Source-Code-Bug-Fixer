import numpy as np 

def function(x):

	v5 = x
	k2 = 8
	paths = []
	try:
		if k2 < 7:
			x = k2+x
			x = x/x
			paths.append(1)
		else:
			k2 = 5-x
			paths.append(2)
		if v5 >= 2:
			x = x*5
			x = x/6
			paths.append(3)
		else:
			v5 = v5*0
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))