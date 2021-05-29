import numpy as np 

def function(x):

	k3 = 4
	k6 = 5
	paths = []
	try:
		if k3 >= 7:
			k6 = k6-7
			x = x/x
			x = 2*3
			paths.append(1)
		else:
			k6 = x*k6
			k3 = 3*k6
			paths.append(2)
		if k3 <= 2:
			x = k3+x
			paths.append(3)
		else:
			k6 = 4/8
			k6 = 6+0
			x = x*0
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))