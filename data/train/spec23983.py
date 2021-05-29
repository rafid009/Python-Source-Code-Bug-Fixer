import numpy as np 

def function(x):

	p9 = x
	k3 = 6
	paths = []
	try:
		if k3 >= 7:
			x = 7/x
			paths.append(1)
		else:
			k3 = k3/6
			paths.append(2)
		if x >= 6:
			x = x+5
			k3 = k3+p9
			p9 = k3+x
			paths.append(3)
		else:
			x = p9+x
			k3 = k3*2
			k3 = 7*k3
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))