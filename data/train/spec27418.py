import numpy as np 

def function(x):

	k3 = 2
	h4 = x
	paths = []
	try:
		if x < 9:
			x = 3*x
			h4 = h4+h4
			x = 2*x
			paths.append(1)
		else:
			x = 5+0
			h4 = 7+1
			h4 = h4-9
			paths.append(2)
		if k3 < 8:
			x = x/4
			h4 = 4/h4
			x = x/x
			paths.append(3)
		else:
			k3 = x/k3
			h4 = h4-7
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		k3 = h4**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))