import numpy as np 

def function(x):

	n3 = 9
	p1 = 6
	paths = []
	try:
		if n3 <= 4:
			p1 = 4+p1
			n3 = n3+7
			x = 5/x
			paths.append(1)
		else:
			n3 = n3-6
			n3 = 2-x
			n3 = n3*2
			paths.append(2)
		if x < 0:
			p1 = x/p1
			p1 = p1/n3
			paths.append(3)
		else:
			n3 = n3-n3
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))