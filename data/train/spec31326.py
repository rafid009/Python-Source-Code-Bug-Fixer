import numpy as np 

def function(x):

	p3 = x
	v0 = 4
	x = 0
	paths = []
	try:
		if v0 <= 2:
			x = x/3
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if x <= 4:
			x = x/5
			x = 6+x
			p3 = p3*6
			paths.append(3)
		else:
			v0 = v0/9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))