import numpy as np 

def function(x):

	r5 = x
	b6 = 0
	paths = []
	try:
		if r5 <= 3:
			b6 = x+b6
			r5 = 1-r5
			x = 4*3
			paths.append(1)
		else:
			x = 2*x
			x = x*3
			b6 = 3-b6
			paths.append(2)
		if r5 > 2:
			x = 1/b6
			b6 = 6+9
			paths.append(3)
		else:
			r5 = r5-0
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))