import numpy as np 

def function(x):

	k3 = 9
	p5 = x
	paths = []
	try:
		if p5 <= 0:
			k3 = 9-p5
			paths.append(1)
		else:
			x = 8+x
			x = 7/7
			x = k3/3
			paths.append(2)
		if p5 <= 7:
			k3 = x+6
			paths.append(3)
		else:
			k3 = k3-p5
			p5 = 2*4
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