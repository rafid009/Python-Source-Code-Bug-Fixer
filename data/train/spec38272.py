import numpy as np 

def function(x):

	p1 = x
	k2 = x
	paths = []
	try:
		if p1 < 5:
			p1 = 6+k2
			x = x-5
			paths.append(1)
		else:
			k2 = k2-7
			paths.append(2)
		if p1 < 9:
			x = x+p1
			x = 5-2
			p1 = 3+p1
			paths.append(3)
		else:
			k2 = k2-5
			p1 = p1+k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))