import numpy as np 

def function(x):

	b3 = 3
	a1 = 8
	x = x
	paths = []
	try:
		if a1 < 7:
			a1 = a1/6
			paths.append(1)
		else:
			a1 = b3-5
			paths.append(2)
		if b3 > 3:
			a1 = 2+5
			paths.append(3)
		else:
			b3 = b3*a1
			b3 = 3+b3
			b3 = b3*2
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))