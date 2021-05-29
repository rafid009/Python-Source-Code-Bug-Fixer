import numpy as np 

def function(x):

	k3 = x
	m5 = x
	paths = []
	try:
		if m5 < 0:
			m5 = k3*m5
			paths.append(1)
		else:
			x = x+1
			m5 = 8-x
			paths.append(2)
		if m5 >= 9:
			x = x*6
			k3 = k3-8
			x = x/9
			paths.append(3)
		else:
			x = 1*2
			k3 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))