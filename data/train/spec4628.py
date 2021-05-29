import numpy as np 

def function(x):

	p7 = 6
	v2 = x
	paths = []
	try:
		if p7 <= 9:
			v2 = v2/x
			v2 = 4+x
			p7 = 7+x
			paths.append(1)
		else:
			x = 8/2
			v2 = 1-9
			x = p7*x
			paths.append(2)
		if p7 >= 0:
			v2 = v2/4
			paths.append(3)
		else:
			x = x/6
			x = x*2
			x = x*3
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		p7 = v2**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))