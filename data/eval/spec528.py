import numpy as np 

def function(x):

	k3 = 5
	p9 = x
	paths = []
	try:
		if p9 > 6:
			p9 = p9-x
			p9 = p9/3
			p9 = x*5
			paths.append(1)
		else:
			x = p9+x
			p9 = p9-0
			paths.append(2)
		if x <= 5:
			x = x-7
			paths.append(3)
		else:
			p9 = p9/1
			p9 = x+p9
			p9 = k3*k3
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		k3 = p9**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))