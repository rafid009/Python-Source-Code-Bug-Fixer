import numpy as np 

def function(x):

	p2 = 1
	t6 = x
	paths = []
	try:
		if t6 > 0:
			p2 = 0/p2
			t6 = t6*1
			p2 = 7*2
			paths.append(1)
		else:
			p2 = 0-p2
			x = x-9
			paths.append(2)
		if p2 >= 2:
			p2 = p2-p2
			paths.append(3)
		else:
			p2 = t6*p2
			t6 = t6-7
			x = x/3
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))