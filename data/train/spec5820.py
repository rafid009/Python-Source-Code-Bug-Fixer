import numpy as np 

def function(x):

	p8 = x
	t4 = 9
	paths = []
	try:
		if t4 > 9:
			p8 = 4/p8
			p8 = x+p8
			p8 = p8/6
			paths.append(1)
		else:
			p8 = 4-5
			paths.append(2)
		if p8 <= 2:
			t4 = t4-x
			p8 = 0-p8
			x = 5+x
			paths.append(3)
		else:
			x = p8*x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))