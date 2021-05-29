import numpy as np 

def function(x):

	o9 = x
	p0 = 6
	paths = []
	try:
		if p0 >= 5:
			x = o9/2
			paths.append(1)
		else:
			p0 = p0/2
			paths.append(2)
		if p0 <= 4:
			o9 = o9/4
			o9 = o9+o9
			p0 = p0/7
			paths.append(3)
		else:
			x = x*9
			x = x+9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		p0 = o9**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))