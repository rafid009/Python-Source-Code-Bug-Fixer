import numpy as np 

def function(x):

	p8 = x
	t4 = 1
	paths = []
	try:
		if t4 > 8:
			p8 = p8-7
			x = t4-3
			paths.append(1)
		else:
			t4 = t4-5
			p8 = p8/2
			paths.append(2)
		if p8 < 1:
			x = 0/8
			paths.append(3)
		else:
			p8 = p8-9
			p8 = x*x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))