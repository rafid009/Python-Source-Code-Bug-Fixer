import numpy as np 

def function(x):

	p4 = x
	t2 = x
	paths = []
	try:
		if p4 >= 5:
			p4 = t2-5
			x = t2/t2
			paths.append(1)
		else:
			p4 = 7+p4
			t2 = p4*p4
			paths.append(2)
		if x <= 9:
			p4 = 6*3
			p4 = 0+4
			p4 = 8/x
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))