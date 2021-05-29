import numpy as np 

def function(x):

	k3 = x
	v5 = x
	paths = []
	try:
		if k3 <= 9:
			v5 = 9*v5
			paths.append(1)
		else:
			x = x+v5
			x = x+0
			paths.append(2)
		if v5 > 8:
			k3 = 2*9
			v5 = x/6
			v5 = v5/4
			paths.append(3)
		else:
			x = k3*x
			v5 = 8*v5
			k3 = k3+3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))