import numpy as np 

def function(x):

	f3 = 4
	p1 = x
	paths = []
	try:
		if f3 > 5:
			p1 = 7*1
			x = 6*x
			paths.append(1)
		else:
			x = f3*x
			p1 = 7*p1
			paths.append(2)
		if x >= 9:
			f3 = 7+f3
			p1 = 6-4
			paths.append(3)
		else:
			p1 = 3-p1
			f3 = f3-p1
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