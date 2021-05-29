import numpy as np 

def function(x):

	p9 = 4
	f2 = x
	paths = []
	try:
		if f2 < 1:
			x = 3*x
			paths.append(1)
		else:
			p9 = 3-5
			p9 = 9/x
			paths.append(2)
		if f2 >= 0:
			f2 = f2*f2
			p9 = 0-x
			paths.append(3)
		else:
			f2 = f2*f2
			f2 = f2+7
			x = x*8
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))