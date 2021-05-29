import numpy as np 

def function(x):

	p2 = x
	t1 = 1
	paths = []
	try:
		if x <= 0:
			p2 = p2-1
			p2 = 7+p2
			x = x+t1
			paths.append(1)
		else:
			x = x+t1
			paths.append(2)
		if p2 > 6:
			t1 = t1*x
			x = x+x
			x = x*5
			paths.append(3)
		else:
			t1 = p2-t1
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