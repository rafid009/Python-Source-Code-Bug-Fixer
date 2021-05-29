import numpy as np 

def function(x):

	t1 = 0
	p7 = 8
	paths = []
	try:
		if x <= 5:
			t1 = t1+p7
			p7 = 9/p7
			paths.append(1)
		else:
			x = 5/x
			p7 = p7-1
			paths.append(2)
		if x > 6:
			p7 = p7-x
			x = 2*8
			p7 = 2*p7
			paths.append(3)
		else:
			t1 = 3+1
			x = x*1
			p7 = x+p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))