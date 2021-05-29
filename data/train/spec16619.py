import numpy as np 

def function(x):

	f2 = 4
	p3 = x
	x = x
	paths = []
	try:
		if p3 <= 3:
			f2 = x+p3
			paths.append(1)
		else:
			p3 = x/3
			p3 = p3*f2
			paths.append(2)
		if f2 > 1:
			f2 = f2+f2
			p3 = p3+p3
			x = 1+8
			paths.append(3)
		else:
			x = 0*x
			f2 = 3*9
			x = 3-f2
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))