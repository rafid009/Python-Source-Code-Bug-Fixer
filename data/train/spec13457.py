import numpy as np 

def function(x):

	t4 = x
	p2 = x
	paths = []
	try:
		if p2 >= 1:
			p2 = p2-p2
			x = x+7
			paths.append(1)
		else:
			t4 = 0/t4
			paths.append(2)
		if x <= 2:
			p2 = x+p2
			t4 = t4+x
			x = 1*x
			paths.append(3)
		else:
			t4 = 7-t4
			x = x*4
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))