import numpy as np 

def function(x):

	e5 = x
	b5 = x
	paths = []
	try:
		if b5 > 4:
			x = x*9
			x = 0/6
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x < 2:
			e5 = e5-6
			paths.append(3)
		else:
			x = x+8
			b5 = b5*0
			x = x*9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))