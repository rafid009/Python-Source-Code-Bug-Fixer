import numpy as np 

def function(x):

	t3 = 4
	p2 = 2
	paths = []
	try:
		if x <= 1:
			x = x+x
			t3 = t3+t3
			t3 = t3/4
			paths.append(1)
		else:
			x = 1*x
			t3 = t3*4
			paths.append(2)
		if p2 >= 5:
			p2 = p2-p2
			paths.append(3)
		else:
			t3 = 7/4
			p2 = 6-p2
			p2 = 9+p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))