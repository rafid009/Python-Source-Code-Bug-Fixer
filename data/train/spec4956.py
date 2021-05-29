import numpy as np 

def function(x):

	k3 = 8
	l3 = x
	paths = []
	try:
		if l3 > 2:
			x = x*0
			l3 = l3-2
			k3 = k3*3
			paths.append(1)
		else:
			l3 = 3/x
			k3 = l3*0
			paths.append(2)
		if l3 >= 4:
			l3 = l3/4
			paths.append(3)
		else:
			x = 0-x
			k3 = k3*l3
			k3 = k3-l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		k3 = l3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))