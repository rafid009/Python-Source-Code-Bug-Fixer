import numpy as np 

def function(x):

	b9 = x
	y5 = 3
	paths = []
	try:
		if b9 <= 3:
			b9 = b9*2
			paths.append(1)
		else:
			b9 = 5-9
			x = x*x
			b9 = b9-7
			paths.append(2)
		if y5 > 9:
			x = x-8
			b9 = b9*0
			paths.append(3)
		else:
			b9 = b9/8
			b9 = b9/y5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		y5 = b9**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))