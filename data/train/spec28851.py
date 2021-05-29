import numpy as np 

def function(x):

	p7 = 1
	f5 = x
	paths = []
	try:
		if p7 >= 0:
			p7 = p7+1
			p7 = p7-8
			f5 = f5*6
			paths.append(1)
		else:
			p7 = x/p7
			paths.append(2)
		if x > 5:
			x = 7/x
			paths.append(3)
		else:
			x = x/9
			p7 = p7/9
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))