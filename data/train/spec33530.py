import numpy as np 

def function(x):

	a1 = x
	y2 = 0
	paths = []
	try:
		if x <= 4:
			x = y2+x
			paths.append(1)
		else:
			x = 1*x
			x = x+5
			a1 = a1-5
			paths.append(2)
		if a1 >= 9:
			y2 = a1-y2
			y2 = y2-8
			paths.append(3)
		else:
			x = x*8
			x = x-8
			y2 = a1+8
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))