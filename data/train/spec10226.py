import numpy as np 

def function(x):

	k3 = x
	v6 = 3
	paths = []
	try:
		if k3 < 5:
			x = x+9
			x = 0/7
			v6 = v6-v6
			paths.append(1)
		else:
			x = 5+3
			x = 8-5
			paths.append(2)
		if k3 >= 4:
			x = k3/6
			paths.append(3)
		else:
			k3 = k3*7
			v6 = v6+k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		v6 = k3**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))