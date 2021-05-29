import numpy as np 

def function(x):

	f7 = x
	p1 = x
	paths = []
	try:
		if p1 < 9:
			f7 = f7+9
			p1 = x+p1
			paths.append(1)
		else:
			f7 = f7-f7
			p1 = p1-3
			paths.append(2)
		if x >= 4:
			x = x+3
			paths.append(3)
		else:
			p1 = p1*2
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