import numpy as np 

def function(x):

	p3 = x
	f1 = x
	paths = []
	try:
		if p3 < 0:
			x = x+x
			p3 = 4/p3
			paths.append(1)
		else:
			x = p3-x
			paths.append(2)
		if x <= 3:
			f1 = f1-3
			f1 = 6/f1
			paths.append(3)
		else:
			x = 6+x
			p3 = x+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))