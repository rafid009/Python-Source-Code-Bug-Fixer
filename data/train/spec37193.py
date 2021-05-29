import numpy as np 

def function(x):

	v3 = 7
	p2 = 8
	paths = []
	try:
		if v3 >= 9:
			x = 3*x
			x = 0+x
			paths.append(1)
		else:
			x = x+1
			p2 = p2/x
			p2 = 7-p2
			paths.append(2)
		if v3 < 9:
			x = v3-4
			x = 7/x
			v3 = 7+8
			paths.append(3)
		else:
			p2 = 1-p2
			x = x+v3
			v3 = 3-x
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		v3 = p2**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))